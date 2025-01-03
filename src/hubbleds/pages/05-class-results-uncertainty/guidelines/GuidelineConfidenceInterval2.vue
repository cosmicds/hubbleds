<template>
  <scaffold-alert
    title-text="Select Best Value"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
    <p>
      Some possibilities are the range that encompass the inner 50%, 68%, or 95% of all measurements.
    </p>
    <p>
      Click the switches to display each percentage range in the histogram. Data points outside the percentage range will be grayed out. 
    </p>
    <p>
      Click <v-icon>mdi-help-circle-outline</v-icon> to learn more about how the percentage ranges are determined.
    </p>
    <p>
      (Note: We do not highlight your own age measurement here to avoid cluttering the viewer.)
    </p>

    </div>
  </scaffold-alert>
</template>

