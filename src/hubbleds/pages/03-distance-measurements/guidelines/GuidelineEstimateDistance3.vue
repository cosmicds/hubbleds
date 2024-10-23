<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto angsize_alert"
    max-width="800"
    elevation="6"
    header-text="Estimate Distance"
    :next-text="state_view.fill_values ? 'next' : 'calculate'"
    @back="back_callback()"
    @next="() => {
      const expectedAnswers = [state_view.meas_theta];
      if (state_view.fill_values) {
        next_callback();
      }
      
      if (validateAnswersJS(['gal_ang_size'], expectedAnswers)) {
        next_callback();
        set_distance(state_view.meas_theta);
      }
    }"
    :can-advance="can_advance"
  >
    <div
      class="mb-4"
      v-intersect="typesetMathJax"
    >
      <p>
        Enter the <b>angular size</b> of your galaxy in <b>arcseconds</b> in the box.
      </p>
      <div
        v-if="!state_view.fill_values"
        class="JaxEquation my-8"
      >
        $$ D = \frac{ {{ Math.round(state_view.distance_const) }} }{\bbox[#FBE9E7]{\input[gal_ang_size][]{}}} $$
      </div>
      <div
        v-else
        class="JaxEquation my-8"
      >
      $$ D = \frac{ {{ Math.round(state_view.distance_const) }} }{\textcolor{black}{\colorbox{#FFAB91}{ {{ (state_view.meas_theta).toFixed(0) }} } } } \text{ Mpc}$$
      </div>
      <v-divider role="presentation"></v-divider>
      <div
        class="font-weight-medium mt-3"
      >
        Click <b>CALCULATE</b> to divide and find the estimated distance to your galaxy.
      </div>
      <v-divider role="presentation" class="mt-3"></v-divider>
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
                $$ D = \frac{ {{ Math.round(state_view.distance_const) }} }{\theta \text{ (in arcsec)}} \text{ Mpc}$$
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col>
              \(D\)
            </v-col>
            <v-col
              cols="10"
            >
              distance to your galaxy, in Mpc
            </v-col>
          </v-row>
          <v-row
            no-gutters
            class="my-1"
          >
            <v-col
              cols="2"
            >
              \(&theta;\)
            </v-col>
            <v-col
              cols="10"
            >
              angular size of your galaxy, in arcseconds
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
    <v-divider
      class="my-4"
      v-if="failedValidation"
    >
    </v-divider>
    <v-alert
      v-if="failedValidation"
      dense
      color="info darken-1"
    >
      Not quite. Make sure you are entering the value for the highlighted galaxy. The angular size column is labeled &theta;, in arcseconds.
    </v-alert>
  </scaffold-alert> 
</template>

<script>
module.exports = {

  data: function() {
    return {
      failedValidation: false
    }
  },

  methods: {
    typesetMathJax(entries, _observer, intersecting) {
      if (intersecting) {
        MathJax.typesetPromise(entries.map(entry => entry.target));
      }
    },

    getValue(inputID) {
      const input = document.getElementById(inputID);
      if (!input) { return null; }
      return input.value;
    },

    parseAnswer(inputID) {
      return parseFloat(this.getValue(inputID).replace(/,/g,''));
    },

    validateAnswersJS(inputIDs, expectedAnswers) {
      return inputIDs.every((id, index) => {
        const value = this.parseAnswer(id);
        this.failedValidation = (value && value === expectedAnswers[index]) ? false : true;
        console.log("expectedAnswer", expectedAnswers);
        console.log("entered value", value);
        return value && value === expectedAnswers[index];
      });
    }
  }
};
</script>

<style>

.JaxEquation .MathJax {
  margin: 16px auto !important;
}

mjx-mfrac {
  margin: 0 4px !important;
}

mjx-mstyle {
  border-radius: 5px;
}

.angsize_alert .v-alert {
  font-size: 16px !important;
}

.v-application .legend {
  border: 1px solid white !important;
  max-width: 300px;
  margin: 0 auto 0;
  font-size: 15px !important;
}

#gal_ang_size {
  color:  black;
  font-size: 18px;
  font-family: "Roboto", Arial, Helvetica, sans-serif;
  padding: 3px;
}


</style>
