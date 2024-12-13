<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Skipped Content"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    :speech="speech"
  >
    <div
      class="mb-4"
    >
      <p>
        <span style="font-weight:bold">SKIPPED CONTENT:</span> Shortened DEMO version skips a slideshow with multiple choice questions that ask students to reflect on the behavior of the galaxies in their data set. 
      </p>
      <p> 
        They should notice that every one of their galaxies has a spectral line with an observed wavelength that is longer than the rest wavelength, so they are all moving away from us. Students are asked to think about whether these observations are consistent with the 1920s view of the universe being static and unchanging.
      </p>
    </div>
  </scaffold-alert>
</template>
