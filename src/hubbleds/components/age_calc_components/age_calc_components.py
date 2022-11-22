import ipyvuetify as v
from cosmicds.cds_glue_state import CDSGlueState
from cosmicds.utils import load_template
from echo import add_callback
from traitlets import Bool, Unicode, Float

from ...utils import AGE_CONSTANT


class AgeCalc(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    state = CDSGlueState().tag(sync=True)
    story_state = CDSGlueState().tag(sync=True)
    failedValidation3 = Bool(False).tag(sync=True)
    failedValidationAgeRange = Bool(False).tag(sync=True)
    age_const = Float().tag(sync=True)
    hint1_dialog = Bool(False).tag(sync=True)
    hint2_dialog = Bool(False).tag(sync=True)
    hint3_dialog = Bool(False).tag(sync=True)
    best_guess = Unicode().tag(sync=True)
    low_guess = Unicode().tag(sync=True)
    high_guess = Unicode().tag(sync=True)
    short_one = Unicode().tag(sync=True)
    short_two= Unicode().tag(sync=True)
    short_other = Unicode().tag(sync=True)

    def __init__(self, filename, path, stage_state, story_state, *args, **kwargs):
        self.state = stage_state
        self.story_state = story_state
        self.age_const = AGE_CONSTANT
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)

        add_callback(self.story_state, 'responses', self._update_guesses)

    def _update_guesses(self, responses):
        if '4' in responses:
            r4 = responses['4']
            self.best_guess = r4.get('best-guess-age', "")
            self.low_guess = r4.get('likely-low-age', "")
            self.high_guess = r4.get('likely-high-age', "")
            self.short_one = r4.get('shortcoming-1', "")
            self.short_two = r4.get('shortcoming-2', "")
            self.short_other = r4.get('other-shortcomings', "")

