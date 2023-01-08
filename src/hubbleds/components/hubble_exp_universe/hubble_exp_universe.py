import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template
from glue_jupyter.state_traitlets_helpers import GlueState
from ipywidgets import widget_serialization, DOMWidget


# theme_colors()

class HubbleExp(v.VuetifyTemplate):
    template = load_template(
        "hubble_exp_universe_slideshow.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(4).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    opened = Bool(False).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)
    interactSteps = List([1]).tag(sync=True)
    layer_viewer = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    hubble_race_viewer = Instance(DOMWidget).tag(sync=True, **widget_serialization)

    _titles = [
        "Hubble's Discovery",
        "A Running Race",
        "Runner's Velocities vs. Distances",
        "Age of the Universe"
    ]
    _default_title = "Hubble's Discovery"

    def __init__(self, viewers, *args, **kwargs):
        self.currentTitle = self._default_title
        self.hubble_race_viewer = viewers[0]
        self.layer_viewer = viewers[1]

        def update_title(change):
            index = change["new"]
            print("step:", index)
            if index in range(len(self._titles)):
                self.currentTitle = self._titles[index]
            else:
                self.currentTitle = self._default_title

        self.observe(update_title, names=["step"])

        super().__init__(*args, **kwargs)
