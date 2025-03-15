<template>
  <scaffold-alert
    title-text="Second Measurement Comparison"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >
    <div class="mb-4">
      <p>
        If your new angular size measurement does not fall at the most commonly measured value, that does not mean your new measurement is wrong.
      </p>
      <p>
        The first measurements were made before viewing the tips on how to make accurate measurements, so it is possible that there was a tendency for the first measurements to be too small or too large.
      </p>
      <p>
        Can you think of ways that the first measurements could have a tendency to be wrong, and in which direction?
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
