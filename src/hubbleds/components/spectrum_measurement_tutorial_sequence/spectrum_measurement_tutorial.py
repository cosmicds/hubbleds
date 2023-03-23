import ipyvuetify as v
from pathlib import Path
from traitlets import Int, Bool, Unicode, List, Instance
from cosmicds.utils import load_template
from glue_jupyter.state_traitlets_helpers import GlueState
from ipywidgets import widget_serialization, DOMWidget

from glue_jupyter.link import link, dlink
from echo import add_callback, delay_callback, CallbackProperty
from bqplot import Label
from bqplot.marks import Lines
from cosmicds.utils import vertical_line_mark

from glue_jupyter.bqplot.histogram.layer_artist import BqplotHistogramLayerArtist
from glue_jupyter.bqplot.scatter.layer_artist import BqplotScatterLayerArtist
# theme_colors()

class SpectrumMeasurementTutorialSequence(v.VuetifyTemplate):
    template = load_template("./spectrum_measurement_tutorial.vue", __file__, traitlet=True).tag(sync=True)
    step = Int(0).tag(sync=True)
    length = Int(19).tag(sync=True)
    dialog = Bool(True).tag(sync=True)
    currentTitle = Unicode("").tag(sync=True)
    maxStepCompleted = Int(0).tag(sync=True)
    spectrum_viewer_widget = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    dotplot_viewer_widget = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    example_galaxy_table = Instance(DOMWidget).tag(sync=True, **widget_serialization)
    show_specviewer = Bool(False).tag(sync=True)
    show_dotplot = Bool(True).tag(sync=True)
    show_table = Bool(False).tag(sync=True)

    _titles = [
        "Measurement Tutorial",
    ]
    _default_title = "Specrum Measurement Tutorial"

    def __init__(self, viewer_layouts, *args, **kwargs):
        # self.state = stage_state
        self.currentTitle = self._default_title
        self.dotplot_viewer_widget = viewer_layouts[0]
        self.spectrum_viewer_widget = viewer_layouts[1]
        self.example_galaxy_table = viewer_layouts[2]
        self.dotplot_viewer = self.dotplot_viewer_widget.viewer
        self.spectrum_viewer = self.spectrum_viewer_widget.viewer
        self.first_meas_plotted = False
        self.second_meas_plotted = False
        self.first_meas_line = None
        self.second_meas_line = None
        
        self.element = self.spectrum_viewer.element 
        # Both in angstroms
        H_ALPHA_REST_LAMBDA = 6565  # SDSS calibrates to wavelengths in a vacuum
        MG_REST_LAMBDA = 5172  # The value used by SDSS is actually 5176.7, but that wavelength aligns with an upward bump, so we are adjusting it to 5172 to avoid confusing students. Ziegler & Bender 1997 uses lambda_0 ~ 5170, so our choice is justifiable.

        self.rest = MG_REST_LAMBDA if self.element == 'Mg-I' else H_ALPHA_REST_LAMBDA
        
        super().__init__(*args, **kwargs)
        
        spec_toolbar = self.spectrum_viewer.toolbar
        # turn on tools
        # spec_toolbar.set_tool_enabled("hubble:restwave",True)
        # spec_toolbar.set_tool_enabled("hubble:wavezoom",True)
        if self.dialog:
            spec_toolbar.set_tool_enabled("bqplot:home",True)
        
        # save the original axis limits so we can reset them later
        self.spectrum_viewer_axis_limits = self.spectrum_viewer.state.x_min, self.spectrum_viewer.state.x_max
        
        link((self.dotplot_viewer.state, 'x_min'), (self.spectrum_viewer.state, 'x_min'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_max'), (self.spectrum_viewer.state, 'x_max'), self.v2w,  self.w2v)
        link((self.dotplot_viewer.state, 'x_min'), (self.spectrum_viewer.state, 'x_min'), self.v2w,  self.w2v)
        
        for val in ['x_min','x_max']:
            add_callback(self.dotplot_viewer.state, val ,self.redraw_dotplot_limits)
            add_callback(self.spectrum_viewer.state, val ,self.redraw_dotplot_limits)
        
        

        
    def vue_reset_spectrum_viewer_limits(self, data = None):
        """
        reset spectrum viewer axis limits 
        
        functions referenced in a vue template requite two inputs, self and data
        data is a dictionary (i think)
        
        adding vue_ to the front of the function name allows it to be called from the associated vue template
        such as <v-btn text @click="() => { reset_spectrum_viewer_limits() }">
        """
        # self.spectrum_viewer.state.x_min = self.spectrum_viewer_axis_limits[0]
        # self.spectrum_viewer.state.x_max = self.spectrum_viewer_axis_limits[1]
        # self.spectrum_viewer.toolbar.set_tool_enabled("hubble:wavezoom", True)
        self.spectrum_viewer.state.reset_limits()
        
    def vue_add_first_measurement(self, change = None):
        if not self.first_meas_plotted:
            data = self.example_galaxy_table._glue_data.to_dataframe()
            data = data[data['measurement_number'] == 'first']
            vel = data['velocity'].values[0]
            if (vel == 0) or (vel is None):
                vel = 20_000
            self.first_meas_line = self.vertical_line_mark(self.dotplot_viewer, vel, '#ff0000','first measurment')
            
            self.dotplot_viewer.figure.marks = self.dotplot_viewer.figure.marks + [self.first_meas_line]
            
            self.first_meas_plotted = True
        
    def vue_add_second_measurement(self, change = None):
        if not self.second_meas_plotted:
            data = self.example_galaxy_table._glue_data.to_dataframe()
            data = data[data['measurement_number'] == 'second']
            try:
                vel = data['velocity'].values[0]
            except KeyError:
                vel = 30_000
            if (vel == 0) or (vel is None):
                vel = 10_000
            self.second_meas_line = self.vertical_line_mark(self.dotplot_viewer, vel, '#00ff00','second measurment')
            
            self.dotplot_viewer.figure.marks = self.dotplot_viewer.figure.marks + [self.second_meas_line]
            self.second_meas_plotted = True
    
    def redraw_dotplot_limits(self, change = None): 
        with delay_callback(self.dotplot_viewer.state, 'hist_x_min', 'hist_x_max'):
            self.dotplot_viewer.state.hist_x_min = self.dotplot_viewer.state.x_min
            self.dotplot_viewer.state.hist_x_max = self.dotplot_viewer.state.x_max
            
            if self.first_meas_plotted:
                self.dotplot_viewer.figure.marks = self.dotplot_viewer.figure.marks + [self.first_meas_line]
            if self.second_meas_plotted:
                self.dotplot_viewer.figure.marks = self.dotplot_viewer.figure.marks + [self.second_meas_line]
    
    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += step 
        
    def v2w(self, v):
        # convert v from velocity (km/s) to wavelength (Angstroms)
        return self.rest * (1 + v / (3 * (10 ** 5)))
    
    def w2v(self, l):
        # convert x from wavelength (Angstroms) to velocity (km/s)
        return (3 * (10 ** 5) * (l / self.rest - 1))
    
    def toggle_tools(self, change):
        if self.dialog:
            self.spectrum_viewer.toolbar.set_tool_enabled("bqplot:home",True)
            self.spectrum_viewer.toolba.set_tool_enabled("hubble:restwave",True)
            self.spectrum_viewer.toolba.set_tool_enabled("hubble:wavezoom",True)
            
    def vertical_line_mark(self,viewer, x, color, label=None):
        scales = {'x': viewer.figure.scale_x, 'y': viewer.figure.scale_y}
        ymin, ymax = scales['y'].min, scales['y'].max
        
        print(f'Add new veritcal line with x = {x} and color = {color} and (ymin,ymax) = ({ymin},{ymax})')
        return Lines(x=[x,x], y=[ymin, ymax], scales=scales, colors=[color], labels=[label])
    
    def vue_show_all_layers(self, data = None):
        for layer in self.dotplot_viewer.layers:
            layer.visible = True
    
    def vue_toggle_first_measurement(self, data = None):
        self.dotplot_viewer.layers[1].visible = not  self.dotplot_viewer.layers[1].visible
        self.redraw_dotplot_limits()
    
    def vue_toggle_second_measurement(self, data = None):
        self.dotplot_viewer.layers[2].visible = not self.dotplot_viewer.layers[2].visible
        self.redraw_dotplot_limits()

    def vue_set_x_axis_limits(self, data = None):
        self.dotplot_viewer.state.x_min = data['xmin']
        self.dotplot_viewer.state.x_max = data['xmax']
        self.redraw_dotplot_limits()