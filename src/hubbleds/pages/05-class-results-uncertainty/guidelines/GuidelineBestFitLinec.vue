<template>
  <scaffold-alert
    title-text="Best Fit Line"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-chart-timeline-variant</v-icon></v-btn> to show best fit.
    </template>

    <div class="mb-4">
      <p>
        <!-- Now  -->
        Let's look at the best-fit line for your class's data. 
        <!-- and see how that compares with your trend line. -->
      </p>
      <p>
        Click on <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-chart-timeline-variant</v-icon></v-btn> in the Toolbar to display the best fit line.
      </p>
    </div>
  </scaffold-alert>
</template>
