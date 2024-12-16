<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Observed Wavelength"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-select-search</v-icon></v-btn> to activate tool. Click and drag across the red <b>{{ state_view.selected_example_galaxy.element }} </b> marker to zoom in.
    </template>

    <div
      class="mb-4"
    >
      <p
        v-if=!state_view.zoom_tool_active>  
        To improve the precision in your measurement, zoom in to the wavelength range around the {{ state_view.selected_example_galaxy.element }} line using the <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-select-search</v-icon></v-btn>  icon in the toolbar.
      </p>
      <p
        v-if=state_view.zoom_tool_active>  
        Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-cached</v-icon></v-btn> to reset the view to the full range of wavelengths.
      </p>
      <p>
        <b>Tip:</b> You can re-measure the wavelength as many times as you like. 
      </p>
    </div>
  </scaffold-alert>
</template>
