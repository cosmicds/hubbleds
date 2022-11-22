import ipyvuetify as v
from cosmicds.cds_glue_state import CDSGlueState
from cosmicds.utils import load_template
from traitlets import Bool, Unicode


class TrendsData(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    state = CDSGlueState().tag(sync=True)
    define_trend = Bool(False).tag(sync=True)

    def __init__(self, filename, path, state, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)
