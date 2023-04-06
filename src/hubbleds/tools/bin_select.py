from glue_jupyter.bqplot.common.tools import BqplotSelectionTool
from glue.config import viewer_tool
from echo import CallbackProperty

from glue.config import viewer_tool
from glue_jupyter.bqplot.common.tools import INTERACT_COLOR

from contextlib import nullcontext


from bqplot.interacts import BrushIntervalSelector, IndexSelector

from glue.core.roi import RangeROI
from glue.core.subset import RangeSubsetState
from glue.config import viewer_tool
import numpy as np


# this decorator tells glue this is a viewer tool, so it knows what to do with
# all this info
@viewer_tool
class BinSelect(BqplotSelectionTool):
    icon = 'glue_xrange_select'
    mdi_icon = "mdi-select-compare"
    tool_id = 'hubble:binselect'
    action_text = 'Select fully enclosed bins'
    tool_tip = 'Select fully enclosed bins'
    tool_activated = CallbackProperty(False)
    x_min = CallbackProperty(0)
    x_max = CallbackProperty(0)
    

    def __init__(self, viewer, **kwargs):

        super().__init__(viewer, **kwargs)

        self.interact = BrushIntervalSelector(scale=self.viewer.scale_x,
                                              color=INTERACT_COLOR)

        self.interact.observe(self.update_selection, "brushing")

    def update_selection(self, *args):
        with self.viewer._output_widget or nullcontext():
            bins = self.viewer.state.bins
            bin_centers = (bins[:-1] + bins[1:]) / 2
            if self.interact.selected is not None:
                x = self.interact.selected
                if x is not None and len(x):
                    print(x)
                    if min(x) != max(x):
                        left = np.searchsorted(bin_centers, min(x), side='left')
                        right = np.searchsorted(bin_centers, max(x), side='right')
                        x = bins[left], bins[right]
                    self.x_min = min(x)
                    self.x_max = max(x)
                    roi = RangeROI(min=min(x), max=max(x), orientation='x')
                    self.viewer.apply_roi(roi)
            self.interact.selected = None
        

    def activate(self):
        with self.viewer._output_widget or nullcontext():
            self.interact.selected = None
        super().activate()
        self.tool_activated = True
    




# this decorator tells glue this is a viewer tool, so it knows what to do with
# all this info
@viewer_tool
class SingleBinSelect(BqplotSelectionTool):
    icon = 'glue_crosshair'
    mdi_icon = "mdi-cursor-default-click"
    tool_id = 'hubble:onebinselect'
    action_text = 'Select a bins'
    tool_tip = 'Select a bins'
    tool_activated = CallbackProperty(False)
    x = CallbackProperty(0)
    

    def __init__(self, viewer, **kwargs):

        super().__init__(viewer, **kwargs)
        
        self.interact = None
        

    def activate(self):
        return super().activate()
    
    def deactivate(self):
        return super().deactivate()
   