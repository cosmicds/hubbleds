<template>
  <scaffold-alert
    title-text="Remeasure Galaxy Angular Size"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
        Remeasure galaxy angular size
    </template>
    <div
      class="mb-4"
    >
      <p>
        Remeasure the example galaxy using what you've learned and see how your answer changes.
      </p>
      <p>
        Adjust the brightness using <v-icon>mdi-brightness-6</v-icon> to make sure you catch the faintest parts of the galaxy!
      </p>
      <p>
        (Click the row for the galaxy in the table to select it if it is not already in view.)
      </p>
      
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {

  data: () => ({
    can_advance: false,
  }),
}
</script>