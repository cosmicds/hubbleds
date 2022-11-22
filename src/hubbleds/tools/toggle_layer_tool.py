from echo import CallbackProperty
from glue.config import viewer_tool
from glue.viewers.common.tool import Tool


@viewer_tool
class LayerToggleTool(Tool):
    class_layer_toggled = CallbackProperty(0)

    tool_id = "hubble:togglelayer"
    action_text = "Toggle display of the classes data"
    tool_tip = "Toggle display of the classes data"
    mdi_icon = "mdi-google-classroom"

    base_layer = 'mine'
    class_layer = 'class'

    def __init__(self, viewer, **kwargs):
        super().__init__(viewer, **kwargs)
        self.layer_index = 0
    

    def activate(self):
        # if we have no layers, don't do anything
        if len(self.viewer.layers) > 0:
            self.layer_to_toggle.visible = not self.layer_to_toggle.visible
        self.class_layer_toggled += 1
        
        if self.layer_to_toggle.visible:
            x_att = str(self.viewer.state.x_att)
            y_att = str(self.viewer.state.y_att)
            # run only the first time the layer is toggled on
            if self.class_layer_toggled == 1:
                self.viewer.state.x_att = self.viewer.state.layers_data[self.layer_index].id[x_att]
                self.viewer.state.y_att = self.viewer.state.layers_data[self.layer_index].id[y_att]
                self.viewer.state.reset_limits()
    
    def set_layer_to_toggle(self, layer = None):
        if layer is not None:
            self.layer_to_toggle = layer
            self.layer_index = self.viewer.layers.index(layer)
        else:
            self.layer_to_toggle = self.viewer.layers[self.layer_index]
        
    def _on_view_change(self, event=None):
        pass
