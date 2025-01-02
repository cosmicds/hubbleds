import solara
from typing import Callable, Iterable


@solara.component_vue("PlotlyLayerToggle.vue")
def PlotlyLayerToggle(chart_id: str,
                      layer_indices: Iterable[int],
                      initial_selected: Iterable[int],
                      enabled: Iterable[bool],
                      colors: Iterable[str],
                      labels: Iterable[str],
                      event_layer_toggled: Callable = lambda *args: True,
):
    pass
