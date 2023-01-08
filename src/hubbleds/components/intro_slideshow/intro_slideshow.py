import astropy.units as u
import ipyvuetify as v
from astropy.coordinates import SkyCoord
from cosmicds.utils import load_template
from traitlets import Int, Bool, Unicode

from ...components.exploration_tool import ExplorationTool
from ...utils import GALAXY_FOV


# theme_colors()

class IntroSlideshow(v.VuetifyTemplate):
    template = load_template("intro_slideshow.vue", __file__,
                             traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(7).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    exploration_complete = Bool(False).tag(sync=True)
    intro_complete = Bool(False).tag(sync=True)
    show_team_interface = Bool(False).tag(sync=True)
    target = Unicode("").tag(sync=True)

    _titles = [
        "Welcome to Your Data Story",
        "Astronomy in the 1920's",
        "Explore the Cosmic Sky",
        "What are the Fuzzy Things?",
        "Spiral Nebulae and the Great Debate",
        "Henrietta Leavitt's Discovery",
        "Vesto Slipher and Spectral Data"
    ]
    _default_title = "Welcome to Your Data Story"

    def __init__(self, show_team_interface, *args, **kwargs):
        self.show_team_interface = show_team_interface
        exploration_tool = ExplorationTool()
        exploration_tool1 = ExplorationTool()
        exploration_tool2 = ExplorationTool()
        self.components = {
            'c-exploration-tool': exploration_tool,
            'c-exploration-tool1': exploration_tool1,
            'c-exploration-tool2': exploration_tool2
        }

        # Initialize at M31. (The next/back buttons do this, but do it here too, in case student navigates with slideshow dots.)
        self.vue_go_to_location_tool2({
            "ra": 10.63,
            "dec": 41.27,
            "fov": 6000,
            "instant": True
        })

        self.currentTitle = self._default_title

        def update_title(change):
            index = change["new"]
            if index in range(len(self._titles)):
                self.currentTitle = self._titles[index]
            else:
                self.currentTitle = self._default_title

        self.observe(update_title, names=["step"])

        def update_exploration_complete(change):
            self.exploration_complete = change["new"]

        exploration_tool.observe(update_exploration_complete,
                                 names=["exploration_complete"])

        super().__init__(*args, **kwargs)

    def go_to_location(self, wwt_label, args):
        wwt = self.components[wwt_label].widget
        coordinates = SkyCoord(args["ra"] * u.deg, args["dec"] * u.deg,
                               frame='icrs')
        instant = args.get("instant") or False
        fov_as = args.get("fov", None)
        fov = fov_as * u.arcsec if fov_as else GALAXY_FOV
        self.target = args.get("target", "none")
        wwt.center_on_coordinates(coordinates, fov=fov, instant=instant)

    def vue_go_to_location_tool1(self, args):
        self.go_to_location('c-exploration-tool1', args)

    def vue_go_to_location_tool2(self, args):
        self.go_to_location('c-exploration-tool2', args)
