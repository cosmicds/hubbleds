from cosmicds.phases import Stage
from cosmicds.registries import register_stage
from cosmicds.utils import load_template
from echo import add_callback, CallbackProperty 
from glue.core.state_objects import State
from traitlets import default
from ..utils import IMAGE_BASE_URL

from ..components.two_intro_slideshow import TwoIntroSlideShow


class StageState(State):
    image_location = CallbackProperty(f"{IMAGE_BASE_URL}/stage_two_intro")


@register_stage(story="hubbles_law", index=2, steps=[
    "ANGULAR SIZES"
])
class StageTwoIntro(Stage):

    _state_cls = StageState

    @default('template')
    def _default_template(self):
        return load_template("stage_two_intro.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "2i"

    @default('title')
    def _default_title(self):
        return "Galaxy Distances Intro"

    @default('subtitle')
    def _default_subtitle(self):
        return "An introduction to Angular Distances"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        two_intro_slideshow = TwoIntroSlideShow(self.app_state.show_team_interface,
                                                self.stage_state.image_location)
        self.add_component(two_intro_slideshow, label='py-two-intro-slideshow')
        two_intro_slideshow.observe(self._on_slideshow_complete,
                                    names=['two_intro_complete'])

        # add_callback(self.story_state, 'step_index',
        #         self._on_step_index_update)

    @property
    def slideshow(self):
        return self.get_component('py-two-intro-slideshow')

    def _on_slideshow_complete(self, change):
        if change["new"]:
            self.story_state.stage_index = 3

            # We need to do this so that the stage will be moved forward every
            # time the button is clicked, not just the first
            self.slideshow.two_intro_complete = False

    # this function is no longer called anywhere
    def _on_step_index_update(self, index):
        # Change the marker without firing the associated stage callback
        # We can't just use ignore_callback, since other stuff (i.e. the frontend)
        # may depend on marker callbacks
        self.trigger_marker_update_cb = False
        index = min(index, len(self.stage_state.step_markers) - 1)
        self.stage_state.marker = self.stage_state.step_markers[index]
        self.trigger_marker_update_cb = True
