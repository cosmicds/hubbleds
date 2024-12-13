<template>
  <v-card
    flat
    light
    variant="outlined"
    color="white"
    class="layer_toggle"
  >
    <v-list-item-group
      multiple
      v-model="selected"
    >
      <v-list-item
        v-for="(layer, index) in reversedLayerIndices.filter((_, idx) => enabled[layer_indices.length - 1 - idx])"
        :key="layer_indices.length - 1 - index"
        :value="layer_indices.length - 1 - index"
        color="black"
        @click="toggleVisibility(layer_indices.length - 1 - index)"
      >
        <template v-slot:default="{ active }">
          <v-list-item-content
            class="font-weight-bold"
          >
            {{ labels[layer_indices.length - 1 - index] }}
          </v-list-item-content>

          <v-list-item-action>
            <v-checkbox
              :input-value="selected.includes(layer_indices.length - 1 - index)"
              :color="colors[layer_indices.length - 1 - index]"
              :disabled="!enabled[layer_indices.length - 1 - index]"
            />
          </v-list-item-action>
        </template>

      </v-list-item>

    </v-list-item-group>
  </v-card>
</template>

<script>
export default {
  props: ["chart_id", "layer_indices", "initial_selected", "enabled", "colors", "labels", ],
  data() {
    return {
      element: null,
      selected: [],
    };
  },
  async mounted() {
    await window.plotlyPromise;
    this.getElement();
    this.selected = this.initial_selected || Array.from({length: this.layer_indices.length}, (x, i) => true);
  },
  computed: {
    reversedLayerIndices() {
      return this.layer_indices.slice().reverse();
    }
  },  
  methods: {
    getElement() {
      this.element = document.getElementById(this.chart_id);
    },
    setLayerVisible(index, visible) {
      if (!this.element) {
        this.getElement();
      }
      Plotly.restyle(this.element, { visible }, {}, index);
    },
    toggleVisibility(index) {
      let makeVisible = false;
      if (this.selected.includes(index)) {
        this.selected = this.selected.filter(idx => idx !== index);
      } else {
        this.selected = this.selected.concat([index]);
        makeVisible = true;
      }
      const layerIndex = this.layer_indices[index];
      this.setLayerVisible(layerIndex, makeVisible);
    }
  }
}
</script>

<style scoped>
.v-card {
  border: solid 1px black !important;
}
</style>
