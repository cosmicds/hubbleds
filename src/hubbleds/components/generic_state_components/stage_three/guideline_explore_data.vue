<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Explore Your Data"
    next-text="graph"
    @next="state.marker = 'tre_dat1'"
    :allow-back="false"
  >
    <div
      class="mb-4"
    >
      <p>
        Now, you have a table of velocity and distance data for your galaxies, like Hubble did.
      </p>
      <p>
        Hubble graphed his data with velocity on the y-axis and distance on the x-axis. Let’s do the same with your data and see what it looks like.
      </p>
    </div>

  </scaffold-alert>
</template>

<script>
module.exports = {
  props: ['state']
}
</script>
