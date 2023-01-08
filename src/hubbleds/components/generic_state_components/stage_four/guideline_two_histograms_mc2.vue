<!-- this state.marker = 'two_his2' -->
<template>
  <scaffold-alert
    title-text="Student Histogram vs. Class Histogram"
    @back="
      state.marker = 'unc_sys1';
    "
    @next="
      state.marker = 'lac_bia1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Let’s come back to the 2 histograms of age values for the universe obtained by all students vs. all classes.
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>Which histogram spans a bigger range of ages?</p>
        <mc-radiogroup
          :radio-options="[
            'The histogram of student measurements.',
            'The histogram of class measurements.',
            'The student and class histograms are the same.'
          ]"
          :feedbacks="[
            'That’s right. The student histogram has a bigger range, telling us that there is more random uncertainty in the student measurements than in the class measurements.',
            'Not quite. Look at the x-axis for each histogram. Where does the range of values start and end for each histogram? Try again.',
            'Not quite. Look at the x-axis for each histogram. Where does the range of values start and end for each histogram? Try again.'
          ]"
          :correct-answers="[0]"
          :wrong-answers='[1,2]'
          @select="(state) => { if (state.correct) { $emit('ready'); } }"
          score-tag="histogram-range"
        >
        </mc-radiogroup>
      </v-container>
    </div>
  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
