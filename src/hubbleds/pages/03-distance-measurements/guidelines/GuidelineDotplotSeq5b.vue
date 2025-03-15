<template>
  <scaffold-alert
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
    >

    <div class="mb-4">
      <p>
        Try moving the ends of the measuring tool to different parts of the galaxy and see how your values move within the dot plots below.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
