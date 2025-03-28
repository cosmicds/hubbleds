from astropy.coordinates import SkyCoord
import astropy.units as u

import solara
from solara.toestand import Ref

from hubbleds.components import IntroSlideshowVue
from hubbleds.state import LOCAL_STATE, GLOBAL_STATE

from hubbleds.remote import LOCAL_API
from hubbleds.widgets.exploration_tool.exploration_tool import ExplorationTool
from ..utils import get_image_path, push_to_route

from hubbleds.layout import Layout
from cosmicds.logger import setup_logger

from cosmicds.components import StateEditor
from .component_state import COMPONENT_STATE, IntroSlideshow, Marker

logger = setup_logger("STAGE INTRO")

@solara.component
def Page():
    solara.Title("HubbleDS")
    router = solara.use_router()
    
    loaded_component_state = solara.use_reactive(False)
    async def _load_component_state():
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)
        logger.info("Finished loading component state.")
        loaded_component_state.set(True)

    solara.lab.use_task(_load_component_state)

    async def _write_component_state():
        if not loaded_component_state.value:
            return

        # Listen for changes in the states and write them to the database
        res = LOCAL_API.put_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)
        if res:
            logger.info("Wrote component state to database.")
        else:
            logger.info("Did not write component state to database.")

    solara.lab.use_task(_write_component_state, dependencies=[COMPONENT_STATE.value])

    exploration_tool = ExplorationTool()
    exploration_tool1 = ExplorationTool()
    exploration_tool2 = ExplorationTool()

    exploration_tools = [exploration_tool, exploration_tool1, exploration_tool2]

    def go_to_location(options):
        index = options.get("index", 0)
        tool = exploration_tools[index]
        fov_as = options.get("fov", 216000)
        fov = fov_as * u.arcsec
        ra = options.get("ra")
        dec = options.get("dec")
        instant = options.get("instant", True)
        coordinates = SkyCoord(ra * u.deg, dec * u.deg, frame='icrs')
        tool.go_to_coordinates(coordinates, fov=fov, instant=instant)

    speech = Ref(GLOBAL_STATE.fields.speech)
    step = Ref(COMPONENT_STATE.fields.intro_slideshow_state.step)
    max_step = Ref(COMPONENT_STATE.fields.max_step)

    IntroSlideshowVue(
        step = COMPONENT_STATE.value.intro_slideshow_state.step,
        event_set_step=step.set,
        max_step=COMPONENT_STATE.value.max_step,
        event_set_max_step=max_step.set,
        length = 8,
        titles = [
            "Our Place in the Universe",
            "Answering Questions with Data",
            "Astronomy in the early 1900s",
            "Explore the Cosmic Sky",
            "What are the Fuzzy Things?",
            "Spiral Nebulae and the Great Debate",
            "Henrietta Leavitt's Discovery",
            "Vesto Slipher and Spectral Data"
        ],
        image_location=get_image_path(router, "stage_intro"),
        event_slideshow_finished=lambda _: push_to_route(router, "01-spectra-&-velocity"),
        debug=LOCAL_STATE.value.debug_mode,
        exploration_tool=exploration_tool,
        exploration_tool1=exploration_tool1,
        exploration_tool2=exploration_tool2,
        event_go_to_location=go_to_location,
        speech=speech.value.model_dump(),
        show_team_interface=GLOBAL_STATE.value.show_team_interface
    )
