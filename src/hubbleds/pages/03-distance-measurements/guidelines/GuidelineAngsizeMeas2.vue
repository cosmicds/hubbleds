<template>
  <scaffold-alert
    title-text="Angular Size Measurement"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Your galaxy now appears in the sky viewer. (You may need to wait a few moments for the full-resolution image to load.)
      </p>
      <p>
        If you zoom towards or away from your galaxy, notice that the angular scale (marked by the light blue line on the left) changes.
      </p>
      <p style="font-weight: 300">
        If the galaxy image doesn't load correctly (and it remains very blurry), click 
        <v-btn icon dark x-small disabled class="mx-1 black--text" elevation="2" style="background-color: #CCCCCC;">
          <v-icon style="color:black!important;">mdi-refresh</v-icon>
        </v-btn>
        to reload.
      </p>
    </div>
  </scaffold-alert>
</template>
<script>
</script>
