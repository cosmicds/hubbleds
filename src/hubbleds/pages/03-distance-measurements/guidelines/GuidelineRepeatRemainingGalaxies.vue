<template>
  <!-- TODO: update when students have measurements 
    <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    :title-text="state_view.angular_sizes_total < 5 ? 'Repeat for Remaining Galaxies' : 'Nice Work'"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  > -->
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :scroll-on-mount="scroll_on_mount"
  >
    <template #before-next>
      <span v-if="!state_view.bad_angsize">
        Measure angular size<span v-if="state_view.angular_sizes_total < 4">s</span> for {{ 5 - state_view.angular_sizes_total }} more <span v-if="state_view.angular_sizes_total < 4">galaxies</span><span v-if="state_view.angular_sizes_total == 4">galaxy</span>.
      </span>
      <span v-if="state_view.bad_angsize">
        <b>Remeasure angular size</b>
        <br/>
      </span>
    </template>

    <!-- If there are no bad measurements and measurements are not complete -->
    <div
      class="mb-4"
      v-if="state_view.angular_sizes_total < 5 && !state_view.bad_angsize"
    >
      <p>
        Keeping in mind what you learned about making good measurements, repeat the angular size measurements for each of the remaining galaxies in your table.
      </p>
    </div>

    <!-- If there are any bad measurements -->
    <div
      class="mb-4"
      v-if="state_view.bad_angsize"
    >
      <p>
        Your measured angular size is not within the expected range. Please try again.
      </p>
      <p>
        Ask your instructor if you are not sure where to measure.
      </p>
    </div>

    <!-- If measurements are complete and there are no bad measurements -->  
    <div
      class="mb-4"
      v-if="state_view.angular_sizes_total >= 5 && !state_view.bad_angsize"
    >
      <p>
        You have measured angular sizes for all of your galaxies.
      </p>
      <p>
        You can continue to refine your measurements, or, if you are satisfied, you can move on.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
