<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Select your Galaxies"
    @back="() => { state.marker = 'sel_gal1'; }"
    @next="() => { state.marker = 'cho_row1'; }"
    :can-advance="(state) => state.gals_total === 5"
    :state="state"
  >

  <template #before-next>
    <strong>Select</strong> {{ 5 - state.gals_total }} <span v-if="state.gals_total>0">more</span> <span v-if="state.gals_total < 4">galaxies</span><span v-if="state.gals_total == 4">galaxy</span>.
  </template>

    <div
      v-if="state.gals_total == 0 & !state.gal_selected"
      class="mb-4"
    >
      <p>
        The green dots in the Cosmic Sky Viewer mark the locations of galaxies you can collect data for. 
      </p>
      <p>
        Pan around the sky and click on one of these dots to select that galaxy.
      </p>
    </div>
    <div
      v-if="state.gals_total < 5 & state.gal_selected"
    >
      <p>
        What do you think of this galaxy?
      </p>
      <p>
        If it looks good to you, add it to your galaxy collection.
      </p>
      <p>
        If you’d rather look for another galaxy, reset the view and choose a different green dot.
      </p>
    </div>
    <div
      v-if="state.gals_total == 1 & !state.gal_selected"
      class="mb-4"
    >
      <p>
        Choose another galaxy to enter into your table. You can pan around the sky from where you are or click the <v-btn icon dark small disabled class="mx-1 black--text" elevation="2" style="background-color: #00E676;"><v-icon style="color:black!important;">mdi-cached</v-icon></v-btn> button to reset the view.
      </p>
    </div>
    <div
      v-if="state.gals_total > 1 & state.gals_total < 5 & !state.gal_selected"
      class="mb-4"
    >
      <p>
        Check it out, your table is growing.
      </p>
      <p>
        Keep selecting galaxies until you have 5 rows in your table.
      </p>
    </div>
    <div
      v-if="state.gals_total == 5"
      class="mb-4"
    >
      <p>
        Great, you have all the galaxies that you need and you're now ready to begin making measurements from your data.
      </p>
      <p>
        Let's turn to your table of galaxies.
      </p>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
