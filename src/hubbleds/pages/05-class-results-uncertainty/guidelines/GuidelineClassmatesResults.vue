<template>
  <scaffold-alert
    title-text="Classmates' Data"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
    >
      <p>
        Let’s look at your class's data, student by student. Someone in your class measured the lowest age value for the universe. Someone measured the highest age.
      </p>
      <p>
        Use the slider to scan through the age estimates that each person in your class measured. 
      </p>
      <p>
        Your value appears in {{ state_view.my_color }}, and your classmates' are {{ state_view.my_class_color }}.
      </p>
      <p>
        Click <v-btn icon tile dark x-small disabled class="mx-1" elevation="2" style="background-color: #0277BD; border-radius: 5px;"><v-icon style="color:white!important;">mdi-select-search</v-icon></v-btn> to zoom in to a smaller velocity or distance range.
      </p>
    </div>
  </scaffold-alert>
</template>
