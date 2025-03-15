<template>
  <scaffold-alert
    title-text="Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Choose a response
    </template>
    <div
      class="mb-4"
    >
      <p>
        Based on this graph do you think there is <b>consensus</b> on the distance to this galaxy?
      </p>
      <mc-radiogroup 
        :radio-options="[
          'Yes',
          'No',
          'I am not sure',
          ]"
          :feedbacks="[
          'Yes, there is a wide spread of measurements, but they cluster around a single common value, so you could say there is consensus.',
          'It is true that the values tend to cluster around a single common value, but the spread is so large that you could say there is not consensus.',
          'This one could go either way. It is true that the values tend to cluster around a single common value, so you could say there is consensus, but the spread is so large that you could also say there is not consensus.'
          ]" 
        :neutral-answers="[0, 1, 2]"
        :score-tag="state_view.score_tag"
        @mc-emit="mc_callback($event)"
        :initialization="state_view.mc_score"
      >
      </mc-radiogroup>
          
      <v-btn
        block
        color="deep-orange darken-2"
        @click="
          define_consensus = !define_consensus
        "
      >
        What is consensus?
      </v-btn>
      <v-alert
        class="mt-4 trend-alert"
        v-if="define_consensus"
        dense
        color="info darken-1"
      >
      A set of measurements shows consensus when all of the measurements tend to cluster around a single rather than multiple values.
      </v-alert>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
  
  data() {
    return {
      define_consensus: false,
    };
  },
};
</script>