import solara
from typing import Callable


DEFAULT_HEADERS = [
    {
        "text": "Galaxy Name",
        "align": "start",
        "sortable": False,
        "value": "name",
    },
    {"text": "Element", "value": "element"},
    {
        "text": "&lambda;<sub>rest</sub> (&Aring;)",
        "value": "rest_wave_value",
    },
    {
        "text": "&lambda;<sub>obs</sub> (&Aring;)",
        "value": "obs_wave_value",
    },
    {"text": "Velocity (km/s)", "value": "velocity_value"},
]


@solara.component_vue("DataTable.vue")
def DataTable(
    title: str = "",
    headers: list[dict] = DEFAULT_HEADERS,
    items: list = [],
    selected: list = [],
    highlighted: bool = False,
    button_icon: str = "",
    show_button: bool = False,
    show_select: bool = False,
    event_on_row_selected: Callable = lambda: None,
    event_on_button_pressed: Callable = lambda: None,
):
    pass
