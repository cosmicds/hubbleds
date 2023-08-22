from echo import CallbackProperty, add_callback, callback_property

from cosmicds.phases import CDSState 


class MarkerState(CDSState):
    marker = CallbackProperty("")
    markers = CallbackProperty([])
    indices = CallbackProperty({})
    advance_marker = CallbackProperty(True)
    progress = CallbackProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marker_index = 0
        self.marker = self.markers[0]
        self.indices = {marker: idx for idx, marker in enumerate(self.markers)}
        add_callback(self, 'marker', self._on_marker_update)

    @callback_property
    def marker_backward(self):
        return None

    @callback_property
    def marker_forward(self):
        return None

    @marker_backward.setter
    def marker_backward(self, value):
        index = self.indices[self.marker]
        new_index = min(max(index - value, 0), len(self.markers) - 1)
        self.marker = self.markers[new_index]

    @marker_forward.setter
    def marker_forward(self, value):
        index = self.indices[self.marker]
        new_index = min(max(index + value, 0), len(self.markers) - 1)
        self.marker = self.markers[new_index]

    def marker_before(self, marker):
        return self.indices[self.marker] < self.indices[marker]

    def marker_after(self, marker):
        return self.indices[self.marker] > self.indices[marker]
    
    def marker_reached(self, marker):
        return self.indices[self.marker] >= self.indices[marker]

    def move_marker_forward(self, marker_text, _value=None):
        index = min(self.markers.index(marker_text) + 1, len(self.markers) - 1)
        self.marker = self.markers[index]

    def marker_index(self, marker):
        return self.indices[marker]

    def _on_marker_update(self, marker):
        index = self.indices[marker]
        self.progress = max(index / len(self.markers), self.progress)
