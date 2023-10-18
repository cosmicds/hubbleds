from echo import CallbackProperty, add_callback, callback_property

from cosmicds.phases import CDSState 


class MarkerState(CDSState):
    marker = CallbackProperty("")
    markers = CallbackProperty([])
    n_markers = CallbackProperty(0)
    max_marker_index = CallbackProperty(0)
    indices = CallbackProperty({})
    advance_marker = CallbackProperty(True)
    progress = CallbackProperty(0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marker_index = 0
        self.marker = self.markers[0]
        self.n_markers = len(self.markers)
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
        if value is None:
            return
        index = self.indices[self.marker]
        new_index = min(max(index - value, 0), len(self.markers) - 1)
        self.marker = self.markers[new_index]

    @marker_forward.setter
    def marker_forward(self, value):
        if value is None:
            return
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
        index = self.indices.get(marker, None)
        if index is None:
            return
        self.max_marker_index = max(index, self.max_marker_index)
        self.progress = self.max_marker_index / (len(self.markers) - 1)
