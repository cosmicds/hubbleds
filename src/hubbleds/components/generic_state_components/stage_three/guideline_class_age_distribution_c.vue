<template>
  <scaffold-alert
    header-text="Class Age Distribution"
    @back="
      state.marker = 'cla_age1c';
    "
    @next="
      state.marker = 'con_int2c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Here is a histogram of the class by class age measurements.
      </p>
    </div>
  </scaffold-alert>
</template>

<style>
  .JaxEquation .MathJax {
    margin: 3px auto !important;
  }
</style>