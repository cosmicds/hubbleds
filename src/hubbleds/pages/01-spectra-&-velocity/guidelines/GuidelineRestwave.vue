<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Rest Wavelength"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >

    <template #before-next>
      <b>Click</b> the <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-lambda</v-icon></v-btn> icon in the Spectrum Viewer toolbar
    </template>

    <div
      class="mb-4"
    >
      <p
        v-if="!state_view.lambda_on"      
      >
        The galaxy spectrum has {{ state_view.selected_example_galaxy.element == 'Mg-I' ? 'a' : 'an' }} {{ state_view.selected_example_galaxy.element }} {{ state_view.selected_example_galaxy.element == 'Mg-I' ? 'absorption' : 'emission' }} line marked by a red vertical line on the graph.
      </p>
      <p
        v-if="!state_view.lambda_on"
      >
        The known <b>rest wavelength</b> (&lambda;<sub>rest</sub>) for the line is recorded in your table.
      </p>
      <p
        v-if="!state_view.lambda_on"
      >
        You can toggle the line's rest wavelength on/off to see it overlayed on the graph.
      </p>
      <p
        v-if="state_view.lambda_on"
      >
        The rest wavelength of your line appears in the graph as a vertical dotted line.
      </p>
      <p
        v-if="state_view.lambda_on"
      >
        You can click the <v-btn icon tile dark small disabled class="mx-1" elevation="2" style="background-color: #1565C0; border-radius: 5px;"><v-icon style="color:white!important;">mdi-lambda</v-icon></v-btn> icon again to toggle the rest wavelength back off.
      </p>
    </div>
  </scaffold-alert>
</template>
