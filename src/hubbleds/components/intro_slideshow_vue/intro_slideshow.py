
import solara
import reacton.ipyvuetify as rv
INTRO_SLIDESHOW_LENGTH = 8
@solara.component_vue("IntroSlideshow.vue")
def IntroSlideshowVue(
    step,
    length,
    titles,
    image_location,
    event_set_step,
    max_step,
    event_set_max_step,
    event_slideshow_finished,
    debug,
    exploration_tool,
    exploration_tool1,
    exploration_tool2,
    event_go_to_location,
    speech,
    show_team_interface,
):
    pass
