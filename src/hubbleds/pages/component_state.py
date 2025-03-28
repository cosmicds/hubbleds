import solara
import enum
from pydantic import BaseModel, computed_field
from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker 
from hubbleds.base_component_state import BaseComponentState
from hubbleds.components import INTRO_SLIDESHOW_LENGTH

class Marker(enum.Enum, BaseMarker):
    int_sli1 = enum.auto()
    end_intro1 = enum.auto()

class IntroSlideshow(BaseModel):
    step: int = 0
    max_step_completed: int = 0

class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.int_sli1
    stage_id: str = "introduction"
    intro_slideshow_state: IntroSlideshow = IntroSlideshow()
    
    _max_step: int = 0 # not included in model
    
    @computed_field
    @property
    def total_steps(self) -> int:
        return INTRO_SLIDESHOW_LENGTH
    
    @computed_field
    @property
    def max_step(self) -> int:
        self._max_step = max(self.intro_slideshow_state.step, self._max_step)
        return self._max_step
    
    
    @computed_field
    @property
    def progress(self) -> float:
        return (self.max_step + 1) / self.total_steps


COMPONENT_STATE = solara.reactive(ComponentState())
