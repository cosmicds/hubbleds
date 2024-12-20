<template>
  <scaffold-alert
    title-text="A Hypothetical Galaxy"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        This "best fit galaxy" is a hypothetical galaxy that lies on your best fit line. You can use its distance and velocity to estimate the age of the universe given by the best fit line to your galaxy data. (Any galaxy that lies on this line would give you the same age estimate.)
      </p>

      <v-card class="mb-4">
        <v-card-text>
          Your <span style="font-weight: bold">best fit galaxy</span> has:<br>
          <table class="mt-3 card-table">
            <tr>
              <td style="font-weight: bold">Velocity</td>
              <td style="font-weight: bold">Distance</td>
            </tr>
            <tr>
              <td>{{ state_view.hypgal_velocity }} km/s</td>
              <td>{{ state_view.hypgal_distance }} Mpc</td>
            </tr>
          </table>
        </v-card-text>
      </v-card>
      
      <p>
        Now let's look at the equation that can tell us the age of universe.
      </p>
    </div>
  </scaffold-alert>
</template>