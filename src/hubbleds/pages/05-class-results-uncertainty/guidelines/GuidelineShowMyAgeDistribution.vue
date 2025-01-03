<template>
  <scaffold-alert
    title-text="My Age in Distribution"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Click the box next to  <span style="background-color: white; border-radius : 5px; padding: 3px; color:black!important; font-size: 80%"><b>My Age</b></span>  in the legend panel to show where in the distribution your age measurement lies.
      </p>
    </div>
  </scaffold-alert>
</template>


