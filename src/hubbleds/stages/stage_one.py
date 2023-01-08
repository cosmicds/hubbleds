import logging
from random import sample

import astropy.units as u
from astropy.coordinates import SkyCoord
from cosmicds.components.table import Table
from cosmicds.phases import CDSState
from cosmicds.registries import register_stage
from cosmicds.utils import load_template, update_figure_css, debounce
from echo import add_callback, ignore_callback, CallbackProperty, \
    DictCallbackProperty, ListCallbackProperty, delay_callback
from glue.core import Data
from glue.core.message import NumericalDataChangedMessage
from numpy import isin
from traitlets import default, Bool

from ..components import SpectrumSlideshow, SelectionTool
from ..data.styles import load_style
from ..data_management import SDSS_DATA_LABEL, SPECTRUM_DATA_LABEL, \
    STUDENT_MEASUREMENTS_LABEL
from ..stage import HubbleStage
from ..utils import GALAXY_FOV, H_ALPHA_REST_LAMBDA, IMAGE_BASE_URL, \
    MG_REST_LAMBDA, velocity_from_wavelengths
from ..viewers import SpectrumView

log = logging.getLogger()


class StageState(CDSState):
    gals_total = CallbackProperty(0)
    gals_max = CallbackProperty(5)
    gal_selected = CallbackProperty(False)
    spec_viewer_reached = CallbackProperty(False)
    spec_tutorial_opened = CallbackProperty(False)
    lambda_used = CallbackProperty(False)
    lambda_on = CallbackProperty(False)
    waveline_set = CallbackProperty(False)
    obswaves_total = CallbackProperty(0)
    velocities_total = CallbackProperty(0)
    zoom_tool_activated = CallbackProperty(False)
    completed = CallbackProperty(False)

    doppler_calc_state = DictCallbackProperty({
        'step': 0,
        'length': 6,
        'currentTitle': "Doppler Calculation",
        'failedValidation4': False,
        'failedValidation5': False,
        'interactSteps5': [3, 4],
        'maxStepCompleted5': 0,
        'studentc': 0,
        'student_vel_calc': False,
        'complete': False,
        'titles': [
            "Doppler Calculation",
            "Doppler Calculation",
            "Doppler Calculation",
            "Reflect on Your Result",
            "Enter Speed of Light",
            "Your Galaxy's Velocity",
        ]
    })

    marker = CallbackProperty("")
    indices = DictCallbackProperty()
    image_location = CallbackProperty(f"{IMAGE_BASE_URL}/stage_one_spectrum")
    lambda_rest = CallbackProperty(0)
    lambda_obs = CallbackProperty(0)
    galaxy = DictCallbackProperty()
    reflection_complete = CallbackProperty(False)
    doppler_calc_reached = CallbackProperty(False)
    doppler_calc_dialog = CallbackProperty(
        True)  # Should the doppler calculation be displayed when marker == dop_cal5?
    student_vel = CallbackProperty(0)  # Value of student's calculated velocity
    doppler_calc_complete = CallbackProperty(False)  # Did student finish the doppler calculation?

    markers = ListCallbackProperty([
        'mee_gui1',
        'sel_gal1',
        'sel_gal2',
        'sel_gal3',
        'cho_row1',
        'mee_spe1',
        'spe_tut1',
        'res_wav1',
        'obs_wav1',
        'obs_wav2',
        'rep_rem1',
        'ref_dat1',
        'dop_cal0',
        'dop_cal1',
        'dop_cal2',
        'dop_cal3',
        'dop_cal4',
        'dop_cal5',
        'dop_cal6'
    ])

    step_markers = ListCallbackProperty([
        'mee_gui1',
        'mee_spe1',
        'ref_dat1',
        'dop_cal0',
    ])

    csv_highlights = ListCallbackProperty([
        'sel_gal1',
        'sel_gal2',
        'sel_gal3',
    ])

    table_highlights = ListCallbackProperty([
        'cho_row1',
        'dop_cal3',
        'dop_cal4',
        'dop_cal5',
        'dop_cal6',
    ])

    spec_highlights = ListCallbackProperty([
        'mee_spe1',
        'res_wav1',
        'obs_wav1',
        'obs_wav2',
        'rep_rem1',
        'ref_dat1',
        'dop_cal0',
        'dop_cal1',
        'dop_cal2',
    ])

    _NONSERIALIZED_PROPERTIES = [
        'markers',  # 'indices',
        'step_markers', 'csv_highlights',
        'table_highlights', 'spec_highlights',
        # 'gals_total', 'obswaves_total',
        'velocities_total', 'image_location'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marker = self.markers[0]
        self.indices = {marker: idx for idx, marker in enumerate(self.markers)}

    def marker_before(self, marker):
        return self.indices[self.marker] < self.indices[marker]

    def marker_after(self, marker):
        return self.indices[self.marker] > self.indices[marker]

    def marker_reached(self, marker):
        return self.indices[self.marker] >= self.indices[marker]

    def marker_index(self, marker):
        return self.indices[marker]


@register_stage(story="hubbles_law", index=1, steps=[
    # "Explore celestial sky",
    "COLLECT DATA",
    "MEASURE SPECTRA",
    "REFLECT",
    "CALCULATE VELOCITIES"
])
class StageOne(HubbleStage):
    show_team_interface = Bool(False).tag(sync=True)
    START_COORDINATES = SkyCoord(180 * u.deg, 25 * u.deg, frame='icrs')

    _state_cls = StageState

    @default('template')
    def _default_template(self):
        return load_template("stage_one.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "1"

    @default('title')
    def _default_title(self):
        return "Spectra & Velocities"

    @default('subtitle')
    def _default_subtitle(self):
        return "Perhaps a small blurb about this stage"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.show_team_interface = self.app_state.show_team_interface

        # Set up any Data-based state values
        self._update_state_from_measurements()
        self.hub.subscribe(
            self, NumericalDataChangedMessage,
            filter=lambda msg: msg.data.label == STUDENT_MEASUREMENTS_LABEL,
            handler=self._on_measurements_changed)

        # Set up viewers
        spectrum_viewer = self.add_viewer(
            SpectrumView, label="spectrum_viewer")
        if spectrum_viewer.toolbar.tools.get("hubble:specflag") is not None:
            sf_tool = spectrum_viewer.toolbar.tools["hubble:specflag"]
            add_callback(sf_tool, "flagged", self._on_spectrum_flagged)

        add_velocities_tool = dict(
            id="update-velocities",
            icon="mdi-run-fast",
            tooltip="Fill in velocities",
            disabled=self.stage_state.marker_before(
                'dop_cal6'),
            activate=self.update_velocities)
        galaxy_table = Table(
            self.session,
            data=self.get_data(STUDENT_MEASUREMENTS_LABEL),
            glue_components=['name',
                             'element',
                             'restwave',
                             'measwave',
                             'velocity'],
            key_component='name',
            names=['Galaxy Name',
                   'Element',
                   'Rest Wavelength (Å)',
                   'Observed Wavelength (Å)',
                   'Velocity (km/s)'],
            title='My Galaxies',
            selected_color=self.table_selected_color(
                self.app_state.dark_mode),
            use_subset_group=False,
            single_select=True,  # True for now
            tools=[add_velocities_tool])

        self.add_widget(galaxy_table, label="galaxy_table")
        galaxy_table.row_click_callback = self.on_galaxy_row_click
        galaxy_table.observe(
            self.galaxy_table_selected_change, names=["selected"])

        # Set up components
        sdss_data = self.get_data(SDSS_DATA_LABEL)
        selected = self.get_data(STUDENT_MEASUREMENTS_LABEL).to_dataframe()
        selection_tool = SelectionTool(data=sdss_data,
                                       selected_data=selected,
                                       show_galaxies=self.stage_state.marker_reached("sel_gal1"))
        self.add_component(selection_tool, label='py-selection-tool')
        selection_tool.on_galaxy_selected = self._on_galaxy_selected
        selection_tool._on_reset_view = self._on_selection_viewer_reset
        selection_tool.observe(self._on_selection_tool_flagged,
                               names=['flagged'])
        selection_tool.observe(self._on_selection_tool_selected,
                               names=['selected'])

        spectrum_slideshow = SpectrumSlideshow(self.stage_state.image_location)
        self.add_component(spectrum_slideshow, label='py-spectrum-slideshow')
        spectrum_slideshow.observe(self._spectrum_slideshow_marker_changed,
                                   names=['marker'])
        spectrum_slideshow.observe(self._spectrum_slideshow_tutorial_opened,
                                   names=['opened'])

        add_callback(self.stage_state, 'student_vel',
                     self.add_student_velocity)
        add_callback(self.stage_state, 'completed',
                     self.complete_stage_one)

        # Callbacks
        def update_count(change):
            if self.stage_state.gals_total > 0 and self.stage_state.marker == "sel_gal2":
                self.stage_state.marker = "sel_gal3"

            self.stage_state.gals_total = change["new"]

        selection_tool.observe(update_count, names=['selected_count'])
        add_callback(self.stage_state, 'marker',
                     self._on_marker_update, echo_old=True)
        add_callback(self.story_state, 'step_index',
                     self._on_step_index_update)
        self.trigger_marker_update_cb = True

        self.update_spectrum_style(dark=self.app_state.dark_mode)

        add_callback(self.stage_state, 'doppler_calc_complete',
                     self.enable_velocity_tool)

        spectrum_viewer = self.get_viewer("spectrum_viewer")
        spec_toolbar = spectrum_viewer.toolbar
        restwave_tool = spec_toolbar.tools["hubble:restwave"]
        add_callback(restwave_tool, 'lambda_used', self._on_lambda_used)
        add_callback(restwave_tool, 'lambda_on', self._on_lambda_on)
        wavezoom_tool = spec_toolbar.tools["hubble:wavezoom"]
        add_callback(wavezoom_tool, 'zoom_tool_activated',
                     self._on_zoom_tool_activated)
        spec_toolbar.set_tool_enabled("hubble:restwave",
                                      self.stage_state.marker_reached(
                                          "res_wav1"))
        spec_toolbar.set_tool_enabled("hubble:wavezoom",
                                      self.stage_state.marker_reached(
                                          "obs_wav2"))
        spec_toolbar.set_tool_enabled("bqplot:home",
                                      self.stage_state.marker_reached(
                                          "obs_wav2"))
        if self.stage_state.galaxy:
            self._on_galaxy_update(self.stage_state.galaxy)
        add_callback(self.stage_state, 'galaxy', self._on_galaxy_update)

        # INITIALIZE STATE VARIABLES WHEN LOADING A STORED STATE
        # reset the state variables when we load a story state
        self.stage_state.spec_tutorial_opened = self.stage_state.marker_reached(
            'spe_tut1')
        self.stage_state.spec_viewer_reached = self.stage_state.marker_reached(
            'cho_row1')
        self.stage_state.doppler_calc_reached = self.stage_state.marker_reached(
            'dop_cal3')

        # Initialize viewers to provide story state
        if self.stage_state.marker_reached('sel_gal1'):
            selection_tool.show_galaxies()
            selection_tool.widget.center_on_coordinates(
                self.START_COORDINATES, fov=60 * u.deg, instant=True)

        if self.stage_state.marker_reached("res_wav1"):
            spectrum_viewer.toolbar.set_tool_enabled("hubble:restwave", True)

        if self.stage_state.marker_reached("obs_wav1"):
            spectrum_viewer.add_event_callback(spectrum_viewer._on_mouse_moved,
                                               events=['mousemove'])
            spectrum_viewer.add_event_callback(spectrum_viewer._on_click,
                                               events=['click'])
            spectrum_viewer.add_event_callback(self.on_spectrum_click,
                                               events=['click'])

        if self.stage_state.marker_reached("obs_wav2"):
            spectrum_viewer.toolbar.set_tool_enabled("hubble:wavezoom", True)
            spectrum_viewer.toolbar.set_tool_enabled("bqplot:home", True)

        # Uncomment this to pre-fill galaxy data for convenience when testing later stages
        # self.vue_fill_data()        

    def _on_measurements_changed(self, msg):
        self._update_state_from_measurements_debounced()

    def _update_state_from_measurements(self):
        student_measurements = self.get_data(STUDENT_MEASUREMENTS_LABEL)
        self.stage_state.gals_total = int(student_measurements.size)
        measwaves = student_measurements["measwave"]
        self.stage_state.obswaves_total = measwaves[measwaves != None].size
        velocities = student_measurements["velocity"]
        self.stage_state.velocities_total = velocities[velocities != None].size

    @debounce(wait=2)
    def _update_state_from_measurements_debounced(self):
        self._update_state_from_measurements()

    def _on_marker_update(self, old, new):
        if not self.trigger_marker_update_cb:
            return
        markers = self.stage_state.markers
        advancing = markers.index(new) > markers.index(old)
        if new in self.stage_state.step_markers and advancing:
            self.story_state.step_complete = True
            self.story_state.step_index = self.stage_state.step_markers.index(
                new)
        if advancing and new == "dop_cal6":
            self.stage_state.doppler_calc_complete = True
        if advancing and old == "sel_gal1":
            self.selection_tool.show_galaxies()
            self.selection_tool.widget.center_on_coordinates(
                self.START_COORDINATES, fov=60 * u.deg, instant=True)
        if advancing and old == "sel_gal3":
            self.galaxy_table.selected = []
            self.selection_tool.widget.center_on_coordinates(
                self.START_COORDINATES, instant=True)
        if advancing and new == "cho_row1" and self.galaxy_table.index is not None:
            self.stage_state.spec_viewer_reached = True
            self.stage_state.marker = "mee_spe1"
        if advancing and old == "dop_cal3" and self.galaxy_table.index is not None:
            self.stage_state.doppler_calc_reached = True
            self.stage_state.marker = "dop_cal4"
        if advancing and old == "dop_cal2":
            self.galaxy_table.selected = []
            self.selection_tool.widget.center_on_coordinates(
                self.START_COORDINATES, instant=True)
        if advancing and new == "res_wav1":
            spectrum_viewer = self.get_viewer("spectrum_viewer")
            spectrum_viewer.toolbar.set_tool_enabled("hubble:restwave", True)
        if advancing and new == "obs_wav1":
            spectrum_viewer = self.get_viewer("spectrum_viewer")
            spectrum_viewer.add_event_callback(spectrum_viewer._on_mouse_moved,
                                               events=['mousemove'])
            spectrum_viewer.add_event_callback(spectrum_viewer._on_click,
                                               events=['click'])
            spectrum_viewer.add_event_callback(self.on_spectrum_click,
                                               events=['click'])
        if advancing and new == "obs_wav2":
            spectrum_viewer = self.get_viewer("spectrum_viewer")
            spectrum_viewer.toolbar.set_tool_enabled("hubble:wavezoom", True)
            spectrum_viewer.toolbar.set_tool_enabled("bqplot:home", True)

    def _on_step_index_update(self, index):
        # If we aren't on this stage, ignore
        if self.story_state.stage_index != self.index:
            return

        # Change the marker without firing the associated stage callback
        # We can't just use ignore_callback, since other stuff (i.e. the
        # frontend) may depend on marker callbacks
        self.trigger_marker_update_cb = False
        index = min(index, len(self.stage_state.step_markers) - 1)
        self.stage_state.marker = self.stage_state.step_markers[index]
        self.trigger_marker_update_cb = True

    def _on_galaxy_update(self, galaxy):
        if galaxy:
            self.story_state.load_spectrum_data(galaxy["name"], galaxy["type"])
            self.galaxy_table.selected = [galaxy]

    def _on_galaxy_selected(self, galaxy):
        data = self.get_data(STUDENT_MEASUREMENTS_LABEL)
        is_in = isin(data['name'], galaxy['name'])  # Avoid duplicates
        already_present = is_in.size > 0 and is_in[0]
        if already_present:
            # To do nothing
            return
            # If instead we wanted to remove the point from the student's
            # selection
            # index = next(idx for idx, val in enumerate(component_dict['ID'])
            #              if val == galaxy['ID'])
            # for component, values in component_dict.items():
            #     values.pop(index)
        else:
            filename = galaxy['name']
            gal_type = galaxy['type']
            galaxy.pop("element")
            self.story_state.load_spectrum_data(filename, gal_type)
            self.add_data_values(STUDENT_MEASUREMENTS_LABEL, galaxy)
            self.stage_state.galaxy = galaxy

    def _on_lambda_used(self, used):
        self.stage_state.lambda_used = used

    def _on_lambda_on(self, on):
        self.stage_state.lambda_on = on

    def _on_zoom_tool_activated(self, used):
        self.stage_state.zoom_tool_activated = used

    def _select_from_data(self, dc_name):
        data = self.get_data(dc_name)
        components = [x.label for x in data.main_components]
        measurements = self.get_data(STUDENT_MEASUREMENTS_LABEL)
        need = self.selection_tool.gals_max - measurements.size
        indices = sample(range(data.size), need)
        for index in indices:
            galaxy = {c: data[c][index] for c in components}
            self.selection_tool.select_galaxy(galaxy)

    def complete_stage_one(self, msg):
        with delay_callback(self.story_state, 'stage_index'):
            self.story_state.step_complete = True
            self.story_state.stage_index = 2

    def vue_fill_data(self, _args=None):
        self._select_from_data("dummy_student_data")
        self.galaxy_table.selected = []
        self.selection_tool.widget.center_on_coordinates(
            self.START_COORDINATES, instant=True)
        self.stage_state.marker = "sel_gal3"

    def vue_select_galaxies(self, _args=None):
        self._select_from_data(SDSS_DATA_LABEL)
        self.galaxy_table.selected = []
        self.selection_tool.widget.center_on_coordinates(
            self.START_COORDINATES, instant=True)
        self.stage_state.marker = "sel_gal3"

    def update_spectrum_viewer(self, name, z):
        specview = self.get_viewer("spectrum_viewer")
        specview.toolbar.active_tool = None
        filename = name
        spec_name = filename.split(".")[0]
        data = self.get_data(spec_name)
        self.story_state.update_data(SPECTRUM_DATA_LABEL, data)
        if len(specview.layers) == 0:
            spec_data = self.get_data(SPECTRUM_DATA_LABEL)
            specview.add_data(spec_data)
            specview.figure.axes[0].label = "Wavelength (Angstroms)"
            specview.figure.axes[1].label = "Brightness"
        specview.state.reset_limits()
        self.stage_state.waveline_set = False

        index = self.get_widget("galaxy_table").index
        student_measurements = self.get_data("student_measurements")
        measwave = student_measurements["measwave"][index]

        sdss = self.get_data(SDSS_DATA_LABEL)
        sdss_index = next(
            (i for i in range(sdss.size) if sdss["name"][i] == name), None)
        if sdss_index is not None:
            element = sdss['element'][sdss_index]
            specview.update(name, element, z, previous=measwave)
            restwave = MG_REST_LAMBDA if element == 'Mg-I' else H_ALPHA_REST_LAMBDA
            self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "element",
                                   element, index)
            self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "restwave",
                                   restwave, index)
            self.stage_state.element = element

    def _spectrum_slideshow_marker_changed(self, msg):
        self.stage_state.marker = msg['new']

    def _spectrum_slideshow_tutorial_opened(self, msg):
        self.stage_state.spec_tutorial_opened = msg['new']

    def _on_doppler_dialog_changed(self, msg):
        self.stage_state.doppler_calc_dialog = msg['new']

    def galaxy_table_selected_change(self, change):
        if change["new"] == change["old"]:
            return

        index = self.galaxy_table.index
        if index is None:
            self._empty_spectrum_viewer()
            return
        data = self.galaxy_table.glue_data
        galaxy = {x.label: data[x][index] for x in data.main_components}
        name = galaxy["name"]
        gal_type = galaxy["type"]
        if name is None or gal_type is None:
            return

        self.selection_tool.current_galaxy = galaxy
        self.stage_state.galaxy = galaxy

        # Load the spectrum data, if necessary
        filename = name
        spec_data = self.story_state.load_spectrum_data(filename, gal_type)

        z = galaxy["z"]
        self.story_state.update_data(SPECTRUM_DATA_LABEL, spec_data)
        self.update_spectrum_viewer(name, z)

        if self.stage_state.marker == 'cho_row1':
            self.stage_state.spec_viewer_reached = True
            self.stage_state.marker = 'mee_spe1'

        if self.stage_state.marker == 'dop_cal3':
            self.stage_state.doppler_calc_reached = True
            self.stage_state.marker = 'dop_cal4'

    def on_galaxy_row_click(self, item, _data=None):
        index = self.galaxy_table.indices_from_items([item])[0]
        data = self.galaxy_table.glue_data
        name = data["name"][index]
        gal_type = data["type"][index]
        if name is None or gal_type is None:
            return

        self.selection_tool.go_to_location(data["ra"][index],
                                           data["decl"][index], fov=GALAXY_FOV)
        self.stage_state.lambda_rest = data["restwave"][index]
        self.stage_state.lambda_obs = data["measwave"][index]
        self.stage_state.sel_gal_index = index

    def _on_selection_viewer_reset(self) -> None:
        """ clear selection from galaxy table"""
        self.galaxy_table.selected = []
        self.stage_state.sel_gal_index = None

    def on_spectrum_click(self, event):
        specview = self.get_viewer("spectrum_viewer")
        if event["event"] != "click" or not specview.line_visible:
            return

        new_value = round(event["domain"]["x"], 0)
        index = self.galaxy_table.index
        data = self.galaxy_table.glue_data

        self.stage_state.waveline_set = True
        self.stage_state.lambda_obs = new_value

        if index is not None:
            self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "measwave",
                                   new_value, index)
            self.story_state.update_student_data()

    def vue_add_current_velocity(self, _args=None):
        data = self.get_data(STUDENT_MEASUREMENTS_LABEL)
        index = self.galaxy_table.index
        if index is not None:
            lamb_rest = data["restwave"][index]
            lamb_meas = data["measwave"][index]
            velocity = velocity_from_wavelengths(lamb_meas, lamb_rest)
            self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "velocity",
                                   velocity, index)
            self.story_state.update_student_data()

    def add_student_velocity(self, *args, **kwargs):
        index = self.galaxy_table.index
        velocity = round(self.stage_state.student_vel)
        self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "velocity",
                               velocity, index)

    @property
    def selection_tool(self):
        return self.get_component("py-selection-tool")

    @property
    def slideshow(self):
        return self.get_component('py-spectrum-slideshow')

    def _update_image_location(self, using_voila):
        prepend = "voila/files/" if using_voila else ""
        self.stage_state.image_location = prepend + "data/images/stage_one_spectrum"

    @property
    def galaxy_table(self):
        return self.get_widget("galaxy_table")

    def update_spectrum_style(self, dark):
        spectrum_viewer = self.get_viewer("spectrum_viewer")
        theme_name = "dark" if dark else "light"
        style = load_style(f"default_spectrum_{theme_name}")
        update_figure_css(spectrum_viewer, style_dict=style)

    def _on_dark_mode_change(self, dark):
        super()._on_dark_mode_change(dark)
        self.update_spectrum_style(dark)

    def _empty_spectrum_viewer(self):
        dc_name = SPECTRUM_DATA_LABEL
        spec_data = self.get_data(dc_name)
        data = Data(label=spec_data.label, **{
            c.label: [0] for c in spec_data.main_components
        })
        spectrum_viewer = self.get_viewer("spectrum_viewer")
        self.story_state.update_data(dc_name, data)
        spectrum_viewer.update("", "", 0)

    def _on_selection_tool_flagged(self, change):
        if not change["new"]:
            return
        index = self.galaxy_table.index
        if index is None:
            return
        item = self.galaxy_table.selected[0]
        galaxy_name = item["name"]
        self.remove_measurement(galaxy_name)

    def _on_selection_tool_selected(self, change):
        self.stage_state.gal_selected = change['new']

    def _on_spectrum_flagged(self, flagged):
        if not flagged:
            return
        # index = self.galaxy_table.index
        item = self.galaxy_table.selected[0]
        galaxy_name = item["name"]
        self.remove_measurement(galaxy_name)
        self._empty_spectrum_viewer()

        spectrum_viewer = self.get_viewer("spectrum_viewer")
        if spectrum_viewer.toolbar.tools.get("hubble:specflag") is not None:
            sf_tool = spectrum_viewer.toolbar.tools["hubble:specflag"]
            with ignore_callback(sf_tool, "flagged"):
                sf_tool.flagged = False

    def update_velocities(self, table, tool):
        data = table.glue_data
        for item in table.items:
            index = table.indices_from_items([item])[0]
            if index is not None and data["velocity"][index] is None:
                lamb_rest = data["restwave"][index]
                lamb_meas = data["measwave"][index]
                if lamb_rest is None or lamb_meas is None:
                    continue
                velocity = velocity_from_wavelengths(lamb_meas, lamb_rest)
                self.update_data_value(STUDENT_MEASUREMENTS_LABEL, "velocity",
                                       velocity, index)
        self.story_state.update_student_data()
        table.update_tool(tool)

    def enable_velocity_tool(self, enable):
        if enable:
            tool = self.galaxy_table.get_tool("update-velocities")
            tool["disabled"] = False
            self.galaxy_table.update_tool(tool)
