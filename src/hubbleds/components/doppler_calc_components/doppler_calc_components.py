import ipyvuetify as v
from cosmicds.cds_glue_state import CDSGlueState
from cosmicds.utils import load_template
from echo import delay_callback
from traitlets import Float, Bool, Int, Unicode, List


class DopplerCalc(v.VuetifyTemplate):
    template = Unicode().tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(6).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    state = CDSGlueState().tag(sync=True)
    story_state = CDSGlueState().tag(sync=True)
    failedValidation4 = Bool(False).tag(sync=True)
    failedValidation5 = Bool(False).tag(sync=True)
    interactSteps5 = List([3, 4]).tag(sync=True)
    maxStepCompleted5 = Int(0).tag(sync=True)
    studentc = Float(0).tag(sync=True)
    student_vel_calc = Bool(False).tag(
        sync=True)  # stage_one.py listens for whether this value changes

    _titles = [
        "Doppler Calculation",
        "Doppler Calculation",
        "Doppler Calculation",
        "Reflect on Your Result",
        "Enter Speed of Light",
        "Your Galaxy's Velocity",
    ]
    _default_title = "Doppler Calculation"

    def __init__(self, filename, path, stage_state, story_state, *args, **kwargs):
        self.state = stage_state
        self.story_state = story_state
        super().__init__(*args, **kwargs)
        self.template = load_template(filename, path)
        self.currentTitle = self._default_title

        def update_title(change):
            index = change["new"]
            if index in range(len(self._titles)):
                self.currentTitle = self._titles[index]
            else:
                self.currentTitle = self._default_title

        self.observe(update_title, names=["step"])

    def vue_complete_stage_one(self, _args=None):
        with delay_callback(self.story_state, 'stage_index'):
            self.story_state.step_complete = True
            self.story_state.stage_index = 2
