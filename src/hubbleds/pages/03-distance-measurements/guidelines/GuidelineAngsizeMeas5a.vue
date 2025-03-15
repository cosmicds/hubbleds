<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <span style="background-color: #02838f; border-radius: 5px; padding: 3px; color:white!important;">MEASUREMENT DOS AND DONTS</span> button.
    </template>

    <div
      class="mb-4"
    >
      <p>
        Given the large spread in angular size measurements for the galaxy, click <span style="background-color: #02838f; border-radius: 5px; padding: 3px; color:white!important;">MEASUREMENT DOS AND DONTS</span> for tips on how to ensure the most accurate results.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>