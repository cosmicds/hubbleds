<template>
  <scaffold-alert
    title-text="Class Age Distribution"
    @back="
      state.marker = 'con_int1';
    "
    @next="
      state.marker = 'con_int2';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        When thinking about the range of ages that are most plausible based on your and your classmatesâ€™ measurements, it is helpful to visualize the data in a different way. 
      </p>
      <p>
        This is a <strong>histogram</strong> which displays the distribution of your classmates' age estimates for the universe. The range of age values is shown on the x-axis, and the number of students who measured that value for the age of the universe is shown on the y-axis.
      </p>
    </div>
  </scaffold-alert>
</template>

<style>
  .JaxEquation .MathJax {
    margin: 3px auto !important;
  }
</style>

<script>
module.exports = {
  props: ['state']
}
</script>
