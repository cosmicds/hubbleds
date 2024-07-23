import reacton.ipyvuetify as rv
import solara
from typing import Callable, Optional


@solara.component_vue("LineDrawPlot.vue")
def LineDrawPlot(chart_id: str,
                 active: bool,
                 fit_active: bool=False,
                 event_line_drawn: Optional[Callable]=None,
                 event_line_fit: Optional[Callable[[list[float]], None]]=None,
                 plot_data: Optional[list[dict]]=None,
                 x_axis_label: Optional[str]=None,
                 y_axis_label: Optional[str]=None,
                 height: Optional[int]=None,
                 margins: Optional[dict]=None,
):
    pass


@solara.component
def LineDrawViewer(chart_id: str,
                   plot_data: Optional[list[dict]]=None,
                   title: Optional[str]="Line Draw Viewer",
                   x_axis_label: Optional[str]=None,
                   y_axis_label: Optional[str]=None,
                   viewer_height: Optional[int]=None,
                   plot_margins: Optional[dict]=None,
                   on_line_drawn: Optional[Callable]=None,
                   on_line_fit: Optional[Callable[[list[float]], None]]=None,
                   draw_enabled: Optional[bool]=True,
                   fit_enabled: Optional[bool]=True,):

    draw_active = solara.use_reactive(False)
    fit_active = solara.use_reactive(False)

    def on_draw_clicked():
        fit_active.set(False)
        draw_active.set(not draw_active.value)

    def on_fit_clicked():
        draw_active.set(False)
        fit_active.set(not fit_active.value)

    # If we want to disable the tool after finishing a line draw
    # pass this function to `LineDrawPlot` as `event_line_drawn`
    # def disable(*args):
    #     active.set(False)

    with rv.Card():
        with rv.Toolbar(class_="toolbar", dense=True):
            with rv.ToolbarTitle(class_="toolbar toolbar-title"):
                solara.Text(title)

            rv.Spacer()

            fit_button = solara.IconButton(
                classes=["toolbar"], icon_name="mdi-chart-timeline-variant", on_click=on_fit_clicked,
                disabled=(not fit_enabled)
            )
            
            draw_button = solara.IconButton(
                classes=["toolbar"], icon_name="mdi-message-draw", on_click=on_draw_clicked, 
                disabled=(not draw_enabled)
            )
            
            rv.BtnToggle(v_model="selected", children=[fit_button, draw_button], background_color="primary", borderless=True)

        LineDrawPlot(chart_id=chart_id,
                     active=draw_active.value,
                     fit_active=fit_active.value,
                     event_line_drawn=on_line_drawn,
                     event_line_fit=on_line_fit,
                     plot_data=plot_data,
                     x_axis_label=x_axis_label,
                     y_axis_label=y_axis_label,
                     height=viewer_height,
                     margins=plot_margins,
        )
