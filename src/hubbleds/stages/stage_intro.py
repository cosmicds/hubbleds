from cosmicds.phases import CDSState
from cosmicds.phases import Stage
from cosmicds.registries import register_stage
from cosmicds.utils import load_template
from echo import CallbackProperty
from traitlets import default

from ..components.intro_slideshow import IntroSlideshow
from ..utils import IMAGE_BASE_URL

class StageState(CDSState):
    image_location = CallbackProperty(f"{IMAGE_BASE_URL}/stage_intro")


@register_stage(story="hubbles_law", index=0, steps=[
    "WELCOME"
])
class StageIntro(Stage):

    _state_cls = StageState

    @default('template')
    def _default_template(self):
        return load_template("stage_intro.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "1i"

    @default('title')
    def _default_title(self):
        return "Introduction"

    @default('subtitle')
    def _default_subtitle(self):
        return "An introduction to Hubble's Law"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        intro_slideshow = IntroSlideshow(self.app_state.show_team_interface)
        self.add_component(intro_slideshow, label='py-intro-slideshow')
        intro_slideshow.observe(self._on_slideshow_complete,
                                names=['intro_complete'])

    @property
    def slideshow(self):
        return self.get_component('py-intro-slideshow')

    def _on_slideshow_complete(self, change):
        if change["new"]:
            self.story_state.stage_index = 1

            # We need to do this so that the stage will be moved forward every
            # time the button is clicked, not just the first
            self.slideshow.intro_complete = False
