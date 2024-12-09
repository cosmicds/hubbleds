# solara
import solara
from solara.toestand import Ref
import reacton.ipyvuetify as rv

# cosmicds
from cosmicds.state import BaseState
from cosmicds.components import ScaffoldAlert
from cosmicds.logger import setup_logger

# hubbleds
from hubbleds.remote import LOCAL_API
from hubbleds.base_component_state import (
    transition_to,
    transition_previous,
    transition_next,
)
from hubbleds.state import (
    LOCAL_STATE, 
    GLOBAL_STATE, 
    mc_callback, 
    fr_callback, 
    get_free_response, 
    get_multiple_choice
    )
from .component_state import COMPONENT_STATE, Marker

# glue-jupyter
from glue_jupyter import JupyterApplication

# misc.
from pathlib import Path
from typing import cast
from functools import partial


logger = setup_logger("TEST-STAGE")

GUIDELINE_ROOT = Path(__file__).parent / "guidelines"

@solara.component
def Page():
    
    # === Setup State Loading and Writing ===
    loaded_component_state = solara.use_reactive(False)
    
    async def _load_component_state():
        LOCAL_API.get_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)
        logger.info("Finished loading component state")
        loaded_component_state.set(True)
    
    solara.lab.use_task(_load_component_state)
    
    async def _write_component_state():
        if not loaded_component_state.value:
            return

        # Listen for changes in the states and write them to the database
        LOCAL_API.put_stage_state(GLOBAL_STATE, LOCAL_STATE, COMPONENT_STATE)

        logger.info("Wrote component state to database.")

    solara.lab.use_task(_write_component_state, dependencies=[COMPONENT_STATE.value])
    
    # === Setup Glue ===
    
    def _glue_setup() -> JupyterApplication:
        # NOTE: use_memo has to be part of the main page render. Including it
        #  in a conditional will result in an error.
        gjapp = JupyterApplication(
            GLOBAL_STATE.value.glue_data_collection, GLOBAL_STATE.value.glue_session
        )

        return gjapp

    gjapp = solara.use_memo(_glue_setup)
    
    def _state_callback_setup():
        # We want to minimize duplicate state handling, but also keep the states
        #  independent. We'll set up observers for changes here so that they
        #  automatically keep the states in sync.
        # See Stage 1 for an example of how to do this manually.
        pass

    solara.use_memo(_state_callback_setup)
    
    button_clicked = Ref(COMPONENT_STATE.fields.button_clicked)
    
    # Layout
    rv.Html(tag="h1", children=["Test Page"])
    
    with solara.Card():
        with solara.Div():
            solara.Text(f"mc_scoring: {LOCAL_STATE.value.mc_scoring}")
        with solara.Div():
            solara.Text(f"free_responses: {LOCAL_STATE.value.free_responses}")

    
    # convenience function
    NoInteractScaffoldAlert = partial(
        ScaffoldAlert, 
        event_next_callback=lambda _: transition_next(COMPONENT_STATE),
        event_back_callback=lambda _: transition_previous(COMPONENT_STATE),
        can_advance=COMPONENT_STATE.value.can_transition(next=True)
    )
    
    logger.info(f"Current step: {COMPONENT_STATE.value.current_step}")
    
    with rv.Row():
        
        with rv.Col(cols=4):
            
            NoInteractScaffoldAlert(
                GUIDELINE_ROOT / "guideline_mark1.vue",
                show=COMPONENT_STATE.value.is_current_step(Marker.mark1)
            )

            ScaffoldAlert(
                GUIDELINE_ROOT / "guideline_mark2.vue",
                event_next_callback = lambda _: transition_next(COMPONENT_STATE),
                event_back_callback = lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.mark2),
                event_mc_callback = lambda event: mc_callback(event, LOCAL_STATE, COMPONENT_STATE),
                state_view={
                    'mc_score': get_multiple_choice(LOCAL_STATE, COMPONENT_STATE, 'mc-2'),
                    'score_tag': 'mc-2'
                }
            )
            

            ScaffoldAlert(
                GUIDELINE_ROOT / "guideline_mark3.vue",
                event_next_callback = lambda _: transition_next(COMPONENT_STATE),
                event_back_callback = lambda _: transition_previous(COMPONENT_STATE),
                can_advance=COMPONENT_STATE.value.can_transition(next=True),
                show=COMPONENT_STATE.value.is_current_step(Marker.mark3),
                event_fr_callback = lambda event: fr_callback(event, LOCAL_STATE, lambda: LOCAL_API.put_story_state(GLOBAL_STATE, LOCAL_STATE)),
                state_view={
                    'free_response': get_free_response(LOCAL_STATE, COMPONENT_STATE,'fr-1')
                }
            )
            
            
            NoInteractScaffoldAlert(
                GUIDELINE_ROOT / "guideline_mark4.vue",
                show=COMPONENT_STATE.value.is_current_step(Marker.mark4)
            )
            
        with rv.Col(cols=4):
            
            solara.Button(
                label="Click this to toggle moving to 2nd step",
                on_click=lambda: button_clicked.set(not button_clicked.value),
                disabled=COMPONENT_STATE.value.current_step_at_or_after(Marker.mark2),
                color="primary"
            )
