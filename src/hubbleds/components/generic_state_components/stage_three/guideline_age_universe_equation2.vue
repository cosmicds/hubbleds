<template>
  <scaffold-alert
    title-text="Age of the Universe"
    @back="
      state.marker = 'age_rac1';
    "
    @next="
      state.marker = 'age_uni3';
    "
  >
    <div
      class="mb-4"
      v-intersect="(entries, _observer, intersecting) => { if (intersecting) { MathJax.typesetPromise(entries.map(entry => entry.target)) }}"
    >
      <p>
        In the units astronomers use, we can write this as:
      </p>
      <v-card
        outlined
        class="legend mt-8"
        color="info"
      >
        <v-container>
          <v-row
            no-gutters
          >
            <v-col>
              <div
                class="JaxEquation"
              >
                $$ t \text{ (in Gyr)}= {{ Math.round(state.age_calc_state.age_const) }}  \times \frac{d \text{ (in Mpc)}}{v \text{ (in km/s)}} $$
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              
            >
              \(t\)
            </v-col>
            <v-col
              cols="10"
            >
              age of the universe, in Gyr. (1 Gyr = 1 billion years)
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(d\)
            </v-col>
            <v-col
              cols="10"
            >
              distance the galaxy has traveled (distance to the galaxy, in Mpc)
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(v\)
            </v-col>
            <v-col
              cols="10"
            >
              velocity of the galaxy (in km/s)
            </v-col>
          </v-row>
        </v-container>
      </v-card>
      <p>

      </p>
      <!--

      <p>
        To simplify the units astronomers use, we can write this as:
      </p>
      <p>
        Time (age of universe Gyr) = Distance in Mpc / velocity in km/s * :conversion factor to give time in Gyr:
      </p>
      <p>
        (A Gyr = 1 billion years).
      </p>
      <p>
        Use the distance and velocity of your ???best fit galaxy??? to calculate the age of the universe.
      </p>
      <p>
        Age measured with my dataset = _________ Gyr.
      </p>
      -->
    </div>
  </scaffold-alert>
</template>

<style>
  .JaxEquation .MathJax {
    margin: 20px auto !important;
  }
</style>

<script>
module.exports = {
  props: ['state']
}
</script>
