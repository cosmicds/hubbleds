<template>
  <scaffold-alert
    title-text="Age of the Universe"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        As with the runners, you can use your galaxies’ velocity and distance data to calculate the time when all galaxies were in the same place — the <b>age of the universe</b>.
      </p>
      <p>
        To figure out the age of the universe implied by your whole dataset, we need to imagine a galaxy that is on the best fit line. Because your data may be messy, it is possible that none of your galaxies are on the best-fit line. (Click <b>NEXT</b> to make a galaxy appear on the line.)
      </p>
    </div>
  </scaffold-alert>
</template>
