import solara
import enum
from pydantic import BaseModel, computed_field
from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker 
from hubbleds.base_component_state import BaseComponentState

class Marker(enum.Enum, BaseMarker):
    mea_dis1 = enum.auto()

class DistanceSlideshow(BaseModel):
    step: int = 0
    max_step_completed: int = 0

class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.mea_dis1
    total_steps: int = len(Marker)
    stage_id: str = "distance_introduction"
    distance_slideshow_state: DistanceSlideshow = DistanceSlideshow()
    
    _max_step: int = 0 # not included in model
    
    # computed fields are included in the model when serialized
    @computed_field
    @property
    def max_step(self) -> int:
        self._max_step = max(self.current_step.value, self._max_step) # type: ignore
        return self._max_step
    
    @computed_field
    @property
    def progress(self) -> float:
        # +1 for zero index, -1 for extra step
        return round(100 * (self._max_step + 1) / (self.total_steps))


COMPONENT_STATE = solara.reactive(ComponentState())