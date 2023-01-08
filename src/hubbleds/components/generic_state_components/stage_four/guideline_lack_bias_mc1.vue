<!-- this state.marker = 'lac_bia1' -->
<template>
  <scaffold-alert
    title-text="Which Might Produce a Closer Result?"
    @back="
      state.marker = 'two_his2';
    "
    @next="
      state.marker = 'lac_bia2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Let’s assume for a moment that there is no systematic uncertainty (or bias) in our measurements. That would mean that the true value for the age of the universe should lie within our measurement range, at the middle.
      </p>
      <v-container
        class="px-0"
        fluid
      >
        <p>Is it more likely that any one class would produce a result closer to the true value or that any one student would produce a result closer to the true value?</p>
        <mc-radiogroup
          :radio-options="[
            'The class is more likely to produce a result closer to the true value.',
            'The student is more likely to produce a result closer to the true value.',
            'They are equally likely to to produce a result closer to the true value.'
          ]"
          :feedbacks="[
            'That’s right. The class is more likely to produce a result closer to the true value. Let’s explore why.',
            'Not quite. Think about the width of the ranges of each histogram. Which range is more likely to keep you closer to a true value? Try again.',
            'Not quite. Think about the width of the ranges of each histogram. Which range is more likely to keep you closer to a true value? Try again.'
          ]"
          :correct-answers="[0]"
          :wrong-answers='[1,2]'
          @select="(state) => { if (state.correct) { $emit('ready'); }; }"
          score-tag="closer-results"
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
