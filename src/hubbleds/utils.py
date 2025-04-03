from collections import defaultdict
from astropy import units as u
from astropy.modeling import models, fitting
from numpy import argsort, array, pi

from cosmicds.utils import component_type_for_field, mode, percent_around_center_indices
from pydantic import BaseModel

from glue.core import Data
from numbers import Number
from typing import List, Set, Tuple, TypeVar

from hubbleds.state import StudentMeasurement
from glue.core import Data
from numpy import asarray
import solara
from solara.routing import Router
from solara.server import settings
from pathlib import Path

try:
    from astropy.cosmology import Planck18 as planck
except ImportError:
    from astropy.cosmology import Planck15 as planck

__all__ = [
    "HUBBLE_ROUTE_PATH",
    "MILKY_WAY_SIZE_MPC",
    "H_ALPHA_REST_LAMBDA",
    "MG_REST_LAMBDA",
    "GALAXY_FOV",
    "FULL_FOV",
    "angle_to_json",
    "angle_from_json",
    "age_in_gyr",
    "format_fov",
    "format_measured_angle",
]

HUBBLE_ROUTE_PATH = "hubbles_law"

MILKY_WAY_SIZE_LTYR = 100000 * u.lightyear
MILKY_WAY_SIZE_MPC = MILKY_WAY_SIZE_LTYR.to(u.Mpc).value
DISTANCE_CONSTANT = (
    round(MILKY_WAY_SIZE_MPC * 3600 * 180 / pi / 100) * 100
)  # theta = L/D:  Distance in Mpc = DISTANCE_CONSTANT / theta in arcsec; Round to hundreds to match slideshow notes.

AGE_CONSTANT = round(1.0e6 * u.pc.to(u.km) / (1e9 * u.yr.to(u.s)) / 10) * 10  # t = d/v
HST_KEY_AGE = 12.79687910  # (1/H_0) in Gyr

SPEED_OF_LIGHT = 3.0 * 10**5  # km/s
# Both in angstroms
H_ALPHA_REST_LAMBDA = 6565  # SDSS calibrates to wavelengths in a vacuum
MG_REST_LAMBDA = 5172  # The value used by SDSS is actually 5176.7, but that wavelength aligns with an upward bump, so we are adjusting it to 5172 to avoid confusing students. Ziegler & Bender 1997 uses lambda_0 ~ 5170, so our choice is justifiable.

GALAXY_FOV = 1.5 * u.arcmin
FULL_FOV = 60 * u.deg

PLOTLY_MARGINS = {"l": 60, "r": 20, "t": 20, "b": 60}

IMAGE_BASE_URL = "https://cosmicds.github.io/cds-website/hubbleds_images"

IMAGE_BASE_STATIC_PATH = "/static/public"
def get_image_path(router, sub_path):
    return f"{router.root_path}{IMAGE_BASE_STATIC_PATH}/{sub_path}"

def angle_to_json(angle, _widget):
    return {"value": angle.value, "unit": angle.unit.name}


def angle_from_json(jsn, _widget):
    return jsn["value"] * u.Unit(jsn["unit"])


def age_in_gyr(H0):
    """
    Given a value for the Hubble constant, computes the age of the universe
    in Gyr, based on the Planck cosmology.

    Parameters
    ----------
    H0: float
        The value of the Hubble constant

    Returns
    ----------
    age: numpy.float64
        The age of the universe, in Gyr
    """
    age = planck.clone(H0=H0).age(0)
    unit = age.unit
    return age.value * unit.to(u.Gyr)


def age_in_gyr_simple(H0):
    inv = 1 / H0
    mpc_to_km = u.Mpc.to(u.km)
    s_to_gyr = u.s.to(u.Gyr)
    return round(inv * mpc_to_km * s_to_gyr, 3)


def fit_line(x, y):
    try:
        fit = fitting.LinearLSQFitter()
        line_init = models.Linear1D(intercept=0, fixed={"intercept": True})
        fitted_line = fit(line_init, x, y)
        return fitted_line
    except ValueError as e:
        print(e)
        return None


def format_fov(fov, units=True):
    suffix = " (dd:mm:ss)" if units else ""
    return fov.to_string(unit=u.degree, sep=":", precision=0, pad=True) + suffix


def format_measured_angle(angle):
    if angle == 0:
        return ""
    return angle.to_string(unit=u.arcsec, precision=0)[:-6] + " arcseconds"


def velocity_from_wavelengths(lamb_meas, lamb_rest):
    return round((3 * (10**5) * (lamb_meas / lamb_rest - 1)), 0)


def distance_from_angular_size(theta):
    return round(DISTANCE_CONSTANT / theta, 0)


def data_summary_for_component(data, component_id):
    summary = {
        "mean": data.compute_statistic("mean", component_id),
        "median": data.compute_statistic("median", component_id),
        "mode": mode(data, component_id),
    }
    values = data[component_id]
    percents = [50, 68, 95]
    sorted_indices = argsort(values)

    for percent in percents:
        bottom_index, top_index = percent_around_center_indices(data.size, percent)
        bottom = values[sorted_indices[bottom_index]]
        top = values[sorted_indices[top_index]]
        summary[f"{percent}%"] = (bottom, top)

    return summary

def measurement_list_to_glue_data(measurements: list[StudentMeasurement] | list[dict], label = ""):
    x = []
    for measurement in measurements:
        if isinstance(measurement, StudentMeasurement):
            x.append(measurement.model_dump())
        else:
            x.append(measurement)
    return Data(label = label, **{k: asarray([r[k] for r in x]) for k in x[0].keys()})


M = TypeVar("M", bound=BaseModel)
def models_to_glue_data(items: List[M],
                        label: str | None=None,
                        ignore_components: list[str] | None=None
) -> Data:
    data_dict = {}
    if items:
        t = type(items[0])
        ignore = ignore_components or []
        for field, info in t.model_fields.items():
            if field not in ignore:
                component_type = component_type_for_field(info)
                data_dict[field] = component_type(array([getattr(m, field) for m in items]))
    if label:
        data_dict["label"] = label
    return Data(**data_dict)


def create_single_summary(distances: List[Number], velocities: List[Number]) -> Tuple[float, float]:
    line = fit_line(distances, velocities)
    h0 = line.slope.value
    age = age_in_gyr_simple(h0)
    return h0, age


def make_summary_data(measurement_data: Data,
                      input_id_field: str="id",
                      output_id_field: str | None=None,
                      label: str | None=None
) -> Data:
    dists = defaultdict(list)
    vels = defaultdict(list)
    d = measurement_data["est_dist_value"]
    v = measurement_data["velocity_value"]
    ids: Set[int] = set()

    for i in range(measurement_data.size):
        id_num = measurement_data[input_id_field][i]
        ids.add(id_num)
        dist = d[i]
        vel = v[i]
        if dist is not None and vel is not None:
            dists[id_num].append(dist)
            vels[id_num].append(vel)

    hubbles: List[float] = []
    ages: List[float] = []
    for id_num in ids:
        h0, age = create_single_summary(dists[id_num], vels[id_num])
        hubbles.append(h0)
        ages.append(age)

    data_kwargs: dict = { "hubble_fit_value": hubbles, "age_value": ages }
    output_id_field = output_id_field or input_id_field
    data_kwargs[output_id_field] = list(ids)

    if label:
        data_kwargs["label"] = label

    return Data(**data_kwargs)

def push_to_route(router: Router, location, route: str):
    if route != '/':
        path = Path(f"{router.root_path}/{route}")
        router.push(str(path))
    else:
        location.pathname = settings.main.base_url