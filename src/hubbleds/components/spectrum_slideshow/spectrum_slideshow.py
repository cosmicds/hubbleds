import ipyvuetify as v
from cosmicds.utils import load_template
from traitlets import Int, Bool, Unicode


class SpectrumSlideshow(v.VuetifyTemplate):
    template = load_template("spectrum_slideshow.vue", __file__,
                             traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(11).tag(sync=True)
    dialog = Bool(False).tag(sync=True)
    marker = Unicode().tag(sync=True)
    opened = Bool(False).tag(sync=True)
    image_location = Unicode().tag(sync=True)

    def __init__(self, image_location, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image_location = image_location
