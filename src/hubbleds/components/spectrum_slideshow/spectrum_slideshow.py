import ipyvuetify as v
from cosmicds.cds_glue_state import CDSGlueState
from cosmicds.utils import load_template
from traitlets import Int, Bool


# theme_colors()

class SpectrumSlideshow(v.VuetifyTemplate):
    template = load_template("spectrum_slideshow.vue", __file__,
                             traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(11).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    # currentTitle = Unicode("").tag(sync=True)
    state = CDSGlueState().tag(sync=True)

    # exploration_complete = Bool(False).tag(sync=True)

    def __init__(self, story_state, *args, **kwargs):
        self.state = story_state

        super().__init__(*args, **kwargs)
