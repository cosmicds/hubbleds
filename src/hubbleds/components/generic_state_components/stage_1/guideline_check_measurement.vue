<template>
  <scaffold-alert
    title-text="Check Measurement"
    @back="() => { state.marker_backward = 1; }"
    @next="() => { state.marker_forward = 1; }"
    :state="state"
  >
    <div>
      <p>
        Now that you have measured the velocity of the example galaxy, we need a way to check your result.
      </p>
      <p>
        In science, you can't always look up the "right answer," so we have to use the information available. This doesn't work 100% of the time, but one method is to follow the <strong>wisdom of crowds</strong> and see what others have measured.
      </p>
    </div>
  </scaffold-alert>
</template>


<script>
module.exports = {
 props: ['state']
}
</script>
