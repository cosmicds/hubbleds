<template>
  <scaffold-alert
    title-text="Confidence Interval"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
    <p>
      Other values that were measured by you and your classmates&mdash;besides the most likely age you just identified&mdash;are also possible. 
    </p>
    <p>
    To account for this, you should specify a likely range of possible age values, or <b>confidence interval</b>.
    </p>
    </div>
  </scaffold-alert>
</template>

