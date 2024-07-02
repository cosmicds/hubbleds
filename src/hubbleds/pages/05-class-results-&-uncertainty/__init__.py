from echo import delay_callback
from glue.core.message import NumericalDataChangedMessage
from glue.viewers.common.viewer import Viewer
from glue_jupyter import JupyterApplication
import numpy as np
import solara
from solara.toestand import Ref

from functools import partial
from pathlib import Path
from typing import Dict, Tuple

from cosmicds.viewers import CDSHistogramView, CDSScatterView
from hubbleds.state import LOCAL_STATE, GLOBAL_STATE
from hubbleds.utils import make_summary_data, models_to_glue_data
from .component_state import COMPONENT_STATE
from hubbleds.remote import LOCAL_API

from cosmicds.logger import setup_logger

logger = setup_logger("STAGE 5")


GUIDELINE_ROOT = Path(__file__).parent / "guidelines"


@solara.component
def Page():
    loaded_component_state = solara.use_reactive(False)

    async def _load_component_state():
        # Load stored component state from database, measurement data is
        # considered higher-level and is loaded when the story starts
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        # TODO: What else to we need to do here?
        logger.info("Finished loading component state for stage 4.")
        loaded_component_state.set(True)

    solara.lab.use_task(_load_component_state)
    
    class_data_loaded = solara.use_reactive(False)
    async def _load_class_data():
        class_measurements = LOCAL_API.get_class_measurements(GLOBAL_STATE, LOCAL_STATE)
        measurements = Ref(LOCAL_STATE.fields.class_measurements)
        student_ids = Ref(LOCAL_STATE.fields.stage_5_class_data_students)
        if class_measurements and not student_ids.value:
            ids = list(np.unique([m.student_id for m in class_measurements]))
            student_ids.set(ids)
        measurements.set(class_measurements)
        class_data_loaded.set(True)

    solara.lab.use_task(_load_class_data)


    all_data_loaded = solara.use_reactive(False)
    async def _load_all_data():

        # This data is external to the current class and won't change
        # so there's never a need to load it more than once
        if "All Measurements" not in GLOBAL_STATE.value.glue_data_collection:
            all_measurements, student_summaries, class_summaries = LOCAL_API.get_all_data(LOCAL_STATE)
            measurements = Ref(LOCAL_STATE.fields.all_measurements)
            stu_summaries = Ref(LOCAL_STATE.fields.student_summaries)
            cls_summaries = Ref(LOCAL_STATE.fields.class_summaries)
            measurements.set(all_measurements)
            stu_summaries.set(student_summaries)
            cls_summaries.set(class_summaries)

        all_data_loaded.set(True)

    solara.lab.use_task(_load_all_data)


    default_color = "#3A86FF"
    highlight_color = "#FF5A00"

    def glue_setup() -> Tuple[JupyterApplication, Dict[str, Viewer]]:
        # NOTE: use_memo has to be part of the main page render. Including it
        #  in a conditional will result in an error.
        gjapp = JupyterApplication(
            GLOBAL_STATE.value.glue_data_collection, GLOBAL_STATE.value.glue_session
        )

        layer_viewer = gjapp.new_data_viewer(CDSScatterView, show=False)
        student_slider_viewer = gjapp.new_data_viewer(CDSScatterView, show=False)
        class_slider_viewer = gjapp.new_data_viewer(CDSScatterView, show=False)
        student_hist_viewer = gjapp.new_data_viewer(CDSHistogramView, show=False)
        class_hist_viewer = gjapp.new_data_viewer(CDSHistogramView, show=False)
        viewers = {
            "layer": layer_viewer,
            "student_slider": student_slider_viewer,
            "class_slider": class_slider_viewer,
            "student_hist": student_hist_viewer,
            "class_hist": class_hist_viewer
        }

        def _update_bins(viewer, *args):
            props = ('hist_n_bin', 'hist_x_min', 'hist_x_max')
            with delay_callback(viewer.state, *props):
                layer = viewer.layers[0] # only works cuz there is only one layer 
                component = viewer.state.x_att                   
                xmin = round(layer.layer.data[component].min(), 0) - 0.5
                xmax = round(layer.layer.data[component].max(), 0) + 0.5
                viewer.state.hist_n_bin = int(xmax - xmin)
                viewer.state.hist_x_min = xmin
                viewer.state.hist_x_max = xmax
        
        for viewer in (student_hist_viewer, class_hist_viewer):
            gjapp.data_collection.hub.subscribe(gjapp.data_collection, NumericalDataChangedMessage,
                                                handler=partial(_update_bins, viewer))

        return gjapp, viewers

    gjapp, viewers = solara.use_memo(glue_setup, dependencies=[])


    links_setup = solara.use_reactive(False)
    def _setup_links():
        if links_setup.value:
            return
        student_data = gjapp.data_collection["My Data"]
        class_data = gjapp.data_collection["Class Data"]
        for component in ("est_dist", "velocity"):
            gjapp.add_link(student_data, component, class_data, component)
        links_setup.set(True)

    def _on_class_data_loaded(value: bool):
        if not value:
            return
        
        class_ids = LOCAL_STATE.value.stage_5_class_data_students
        class_data_points = [m for m in LOCAL_STATE.value.class_measurements if m.student_id in class_ids]
        class_data = models_to_glue_data(class_data_points, label="Class Data")
        class_data = GLOBAL_STATE.value.add_or_update_data(class_data)

        layer_viewer = viewers["layer"]
        layer_viewer.add_data(class_data)
        layer_viewer.state.x_axislabel = "Distance (Mpc)"
        layer_viewer.state.y_axislabel = "Velocity"
        layer_viewer.state.x_att = class_data.id['est_dist']
        layer_viewer.state.y_att = class_data.id['velocity']

        if len(class_data.subsets) == 0:
            student_slider_subset = class_data.new_subset(label="student_slider_subset", alpha=1, markersize=10)
        else:
            student_slider_subset = class_data.subsets[0]
        slider_viewer = viewers["student_slider"]
        slider_viewer.state.x_att = class_data.id['est_dist']
        slider_viewer.state.y_att = class_data.id['velocity']
        slider_viewer.state.title = "Stage 5 Class Data Viewer"
        slider_viewer.layers[0].state.visible = False
        slider_viewer.add_subset(student_slider_subset)

        class_summary_data = make_summary_data(class_data,
                                               input_id_field="student_id",
                                               output_id_field="id",
                                               label="Class Summaries")
        class_summary_data = GLOBAL_STATE.value.add_or_update_data(class_summary_data)

        hist_viewer = viewers["student_hist"]
        hist_viewer.state.x_att = class_summary_data.id['age_value']
        hist_viewer.state.title = "My class ages (5 galaxies each)"
        hist_viewer.layers[0].state.color = "red"

        if LOCAL_STATE.value.measurements_loaded.value:
            _setup_links()

    class_data_loaded.subscribe(_on_class_data_loaded)

    def _on_student_data_loaded(value: bool):
        if not value:
            return
        student_data = models_to_glue_data(LOCAL_STATE.value.measurements, label="My Data", ignore_components=["galaxy"])
        student_data = GLOBAL_STATE.value.add_or_update_data(student_data)
        layer_viewer = viewers["layer"]
        layer_viewer.add_data(student_data)

        if class_data_loaded.value:
            _setup_links()

    if LOCAL_STATE.value.measurements_loaded.value:
        _on_student_data_loaded(True)
    else:
        LOCAL_STATE.value.measurements_loaded.subscribe(_on_student_data_loaded)

    def _on_all_data_loaded(value):
        if not value:
            return

        all_measurements = LOCAL_STATE.value.all_measurements
        student_summaries = LOCAL_STATE.value.student_summaries
        class_summaries = LOCAL_STATE.value.class_summaries

        all_data = models_to_glue_data(all_measurements, label="All Student Summaries")
        all_data = GLOBAL_STATE.value.add_or_update_data(all_data)

        student_summ_data = models_to_glue_data(student_summaries, label="All Student Summaries")
        student_summ_data = GLOBAL_STATE.value.add_or_update_data(student_summ_data)

        all_class_summ_data = models_to_glue_data(class_summaries, label="All Class Summaries")
        all_class_summ_data = GLOBAL_STATE.value.add_or_update_data(all_class_summ_data)

        if len(all_data.subsets) == 0:
            class_slider_subset = all_data.new_subset(label="class_slider_subset", alpha=1, markersize=10)
        else:
            class_slider_subset = all_data.subsets[0]

        slider_viewer = viewers["class_slider"]
        slider_viewer.state.x_att = all_data.id['est_dist']
        slider_viewer.state.y_att = all_data.id['velocity']
        slider_viewer.state.title = "Stage 5 All Classes Data Viewer"
        slider_viewer.layers[0].state.visible = False
        slider_viewer.add_subset(class_slider_subset)

        hist_viewer = viewers["class_hist"]
        hist_viewer.state.x_att = all_class_summ_data.id['age_value']
        hist_viewer.state.title = "All class ages (5 galaxies each)"
        hist_viewer.layers[0].state.color = "blue"

    all_data_loaded.subscribe(_on_all_data_loaded)
