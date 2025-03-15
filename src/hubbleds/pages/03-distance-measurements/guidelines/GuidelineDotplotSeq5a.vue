<template>
  <scaffold-alert
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <div class="mb-4">
      <p>
        Your updated measurements are displayed in orange in the distance and angular size dot plots.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>