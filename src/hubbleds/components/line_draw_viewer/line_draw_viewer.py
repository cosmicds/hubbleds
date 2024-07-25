import reacton.ipyvuetify as rv
import solara
from typing import Callable, Optional, Dict


@solara.component_vue("LineDrawPlot.vue")
def LineDrawPlot(chart_id: str,
                 draw_active: bool,
                 fit_active: bool=False,
                 event_line_drawn: Optional[Callable]=None,
                 event_line_fit: Optional[Callable[[Dict],None]] = None,
                 plot_data: Optional[list[dict]]=None,
                 x_axis_label: Optional[str]=None,
                 y_axis_label: Optional[str]=None,
                 height: Optional[int]=None,
                 margins: Optional[dict]=None,
                 display_best_fit_gal: Optional[bool]=False,
                 best_fit_gal_layer_index: Optional[int]=None,
                 clear_class_layer: Optional[bool]=False,
                 clear_drawn_line: Optional[bool]=False,
                 clear_fit_line: Optional[bool]=False,
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
                   on_draw_clicked: Optional[Callable]=None,
                   on_best_fit_clicked: Optional[Callable]=None,
                   on_line_drawn: Optional[Callable]=None,
                   on_line_fit: Optional[Callable[[Dict],None]] = None,
                   draw_enabled: Optional[bool]=True,
                   fit_enabled: Optional[bool]=True,
                   display_best_fit_gal: Optional[bool]=False,
                   best_fit_gal_layer_index: Optional[int]=None,
                   clear_class_layer: Optional[bool]=False,
                   clear_drawn_line: Optional[bool]=False,
                   clear_fit_line: Optional[bool]=False,
                   ):

    draw_active = solara.use_reactive(False)
    fit_active = solara.use_reactive(False)
    # best_fit_active = solara.use_reactive(False)

    def _on_draw_clicked():
        fit_active.set(False)
        draw_active.set(not draw_active.value)
        if on_draw_clicked is not None:
            on_draw_clicked()

    def _on_fit_clicked():
        draw_active.set(False)
        fit_active.set(not fit_active.value)
        if on_best_fit_clicked is not None:
            on_best_fit_clicked()

    # def on_best_fit_clicked():
    #     best_fit_active.set(not best_fit_active.value)

    # If we want to disable the tool after finishing a line draw
    # pass this function to `LineDrawPlot` as `event_line_drawn`
    # def disable(*args):
    #     draw_active.set(False)

    with rv.Card():
        with rv.Toolbar(class_="toolbar", dense=True):
            with rv.ToolbarTitle(class_="toolbar toolbar-title"):
                solara.Text(title)

            rv.Spacer()

            fit_button = solara.IconButton(
                classes=["toolbar"], icon_name="mdi-chart-timeline-variant", on_click=_on_fit_clicked,
                disabled=(not fit_enabled)
            )

            draw_button = solara.IconButton(
                classes=["toolbar"], icon_name="mdi-message-draw", on_click=_on_draw_clicked, 
                disabled=(not draw_enabled)
            )

            # best_fit_button = solara.IconButton(
            #     classes=["toolbar"], icon_name="mdi-star-box-outline", on_click=on_best_fit_clicked, 
            # )

            rv.BtnToggle(v_model="selected", children=[fit_button, draw_button], background_color="primary", borderless=True)

        LineDrawPlot(chart_id=chart_id,
                     draw_active=draw_active.value,
                     fit_active=fit_active.value,
                     event_line_drawn=on_line_drawn,
                     event_line_fit=on_line_fit,
                     plot_data=plot_data,
                     x_axis_label=x_axis_label,
                     y_axis_label=y_axis_label,
                     height=viewer_height,
                     margins=plot_margins,
                     display_best_fit_gal=display_best_fit_gal,
                     best_fit_gal_layer_index=best_fit_gal_layer_index,
                     clear_class_layer=clear_class_layer,
                     clear_drawn_line = clear_drawn_line,
                     clear_fit_line = clear_fit_line,
        )
