<template>
  <scaffold-alert
    title-text="Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Below is the distribution of angular size measurements for this galaxy. Notice the angular size measurements also have a large spread.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
