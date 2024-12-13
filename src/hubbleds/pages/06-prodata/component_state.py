import solara

from pydantic import field_validator

from cosmicds.state import BaseState
from hubbleds.base_marker import BaseMarker
from hubbleds.base_component_state import BaseComponentState
from hubbleds.state import LOCAL_STATE

import enum
from typing import Any

from functools import cached_property

from ...data_management import HUBBLE_1929_DATA_LABEL, HUBBLE_KEY_DATA_LABEL


class Marker(enum.Enum, BaseMarker):
    pro_dat0 = enum.auto()
    pro_dat1 = enum.auto()
    pro_dat2 = enum.auto()
    pro_dat3 = enum.auto()
    pro_dat4 = enum.auto()
    pro_dat5 = enum.auto()
    pro_dat6 = enum.auto()
    pro_dat7 = enum.auto()
    pro_dat8 = enum.auto()
    pro_dat9 = enum.auto()
    sto_fin1 = enum.auto()
    sto_fin2 = enum.auto()
    # sto_fin3 = enum.auto()
    
class ComponentState(BaseComponentState, BaseState):
    current_step: Marker = Marker.pro_dat0
    stage_id: str = "professional_data"
    
    # TODO: I don't think our_age is used anywhere
    our_age: float = 0
    class_age: float = 0
    
    ages_within: float = 0.15
    allow_too_close_correct: bool = True
    
    fit_line_shown: bool = False
    
    

    @field_validator("current_step", mode="before")
    def convert_int_to_enum(cls, v: Any) -> Marker:
        if isinstance(v, int):
            return Marker(v)
        return v
    
    @property
    def pro_dat2_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat1")
    
    @property
    def pro_dat3_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat2")
    
    @property
    def pro_dat4_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat3") 
    
    @property
    def pro_dat5_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat4") #and LOCAL_STATE.value.question_completed("prodata-free-4")
    
    @property
    def pro_dat7_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat6")
    
    @property
    def pro_dat8_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat7") #and LOCAL_STATE.value.question_completed("prodata-free-7")
    
    # @property
    # def pro_dat9_gate(self) -> bool:
    #     return LOCAL_STATE.value.question_completed("prodata-reflect-8a") #and LOCAL_STATE.value.question_completed("prodata-reflect-8b") and LOCAL_STATE.value.question_completed("prodata-reflect-8c")
    
    @property
    def sto_fin1_gate(self) -> bool:
        return LOCAL_STATE.value.question_completed("pro-dat9")
    
    
COMPONENT_STATE = solara.reactive(ComponentState())
