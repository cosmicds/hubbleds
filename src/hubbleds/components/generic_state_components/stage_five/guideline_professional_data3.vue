<!-- # multiple choice -->
<template>
  <guideline-professional-data
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    prev-marker="pro_dat2"
    next-marker="pro_dat4"
    :state="state"
    v-slot:default="{ allowAdvancing }"
    :index="3"
  >
    <div
      class="mb-4"
    >
      <p>
        Whose data set has more random uncertainty?
      </p>
      
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class\'s dataset',
            'Edwin Hubble\'s dataset',
            'It\'s hard to tell',
          ]"
          :feedbacks='[
            "Yes. We can see how much more our data deviates from the best fit line.",
            "It can be hard to tell. One thing to consider is how far off your data is from the best fit line",
            "It can be hard to tell. One thing to consider is how far off your data is from the best fit line",
          ]'
          :correct-answers="[0]"
          :neutral-answers='[1,2]'
          @select="(status) => { if (status.correct) { allowAdvancing(); } }"
          score-tag="pro-dat3"
        >
        </mc-radiogroup>
      </v-container>
    </div>
  </guideline-professional-data>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
