import ipyvuetify as v
from cosmicds.cds_glue_state import CDSGlueState
from cosmicds.utils import load_template
from traitlets import Bool, Unicode, observe


class ProData(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    state = CDSGlueState().tag(sync=True)
    some_state_variable = Bool(False).tag(sync=True)
    can_advance = Bool(False).tag(sync=True)

    def __init__(self, filename, path, state, index, *args, **kwargs):
        self.state = state
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)
        self.index = index
        self.can_advance = self.state.max_prodata_index > self.index

    def _update_index(self):
        self.state.max_prodata_index = max(self.state.max_prodata_index, self.index)

    def vue_advance(self, marker):
        self.state.marker = marker
        self._update_index()

    @observe('can_advance')
    def on_can_advance(self, change):
        if change["new"]:
            self._update_index()
