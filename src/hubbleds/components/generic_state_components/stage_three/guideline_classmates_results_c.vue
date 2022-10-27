<template>
  <scaffold-alert
    header-text="Classmates' Data"
    @back="
      state.marker = 'you_age1c';
    "
    @next="
      state.marker = 'cla_age1c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Now let’s look at age estimates of the universe from other classes who have already completed this data story.
      </p>
      <v-card
        color="secondary"
        class="mb-4"
      >
        <v-card-text>
          Full disclosure for our beta testers: Since there were no students before you, the CosmicDS team acted as "seed students," created galaxies measurements as you have, and grouped our data into "classes."
        </v-card-text>
      </v-card>
      <p>
        Let’s look at the data, class by class. Some class measured the lowest age value for the universe. Some class measured the highest age.
      </p>
      <p>
        Use the slider to scan through the age estimates that each participating class measured. 
      </p>
    </div>
  </scaffold-alert>
</template>
