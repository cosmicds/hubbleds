<!-- # multiple choice -->
<template>
  <guideline-professional-data
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    prev-marker="pro_dat5"
    next-marker="pro_dat7"
    v-slot:default="{ allowAdvancing }"
    :state="state"
    :index="6"
  >
    <div
      class="mb-4"
    >
      Is your age estimate higher or lower than the HST team's estimate?
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class got a higher age estimate than HST',
            'Our class got a lower age estimate than HST',
          ]"
          :feedbacks="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ?
  ['Correct! The slope of best fit for our data is shallower than it is for the HST data', 'Try again! Compare the slope of best fit for our data to the slope for the HST data'] :
  ['Try again! Compare the slope of best fit for our data to the slope for the HST data','Correct! The slope of best fit for our data is steeper than it is for the HST data', ]"
          :correct-answers="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ? [0] : [1]"
          :neutral-answers="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ? [1] : [0]"
          @select="(status) => { if (status.correct) { allowAdvancing(); } }"
          score-tag="pro-dat6"
        >
        </mc-radiogroup>
      <v-card color="secondary">
        <v-card-text>
          It's possible this card is giving incorrect feedback. Talk to a neighbor or instructor if you are unsure.
        </v-card-text>
      </v-card>
      </v-container>
    </div>
  </guideline-professional-data>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
