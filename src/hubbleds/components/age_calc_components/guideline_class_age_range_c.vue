<template>
  <v-alert
    color="info"
    class="mb-4 mx-auto angsize_alert"
    max-width="800"
    elevation="6"
  >
    <h3
      class="mb-4"
    >
      All Classes Age Range
    </h3> 

    <div
      class="mb-4"
      v-intersect="(entries, _observer, intersecting) => { if (intersecting) { MathJax.typesetPromise(entries.map(entry => entry.target)) }}"
    >
      <p>
        Let's consider the range of age estimates for the universe obtained by all the classes who have completed this Data Story.
      </p>
      <p>
        Enter the lowest and highest age estimates within the dataset here:
      </p>
      <div
        class="JaxEquation my-8"
      >
        $$ \text{Lowest age:  } \bbox[#FBE9E7]{\input[low_age][]{} } \text{ Gyr} $$
        $$ \text{Highest age:  } \bbox[#FBE9E7]{\input[high_age][]{} } \text{ Gyr} $$
      </div>
      <v-divider role="presentation"></v-divider>
    </div>
    <v-divider
      class="my-4"
      v-if="failedValidationAgeRange"
    >
    </v-divider>
    <v-alert
      v-if="failedValidationAgeRange"
      dense
      color="info darken-1"
    >
      Not quite. Make sure you are entering the highest and lowest values for the entire dataset. Enter only whole integers.
    </v-alert>
    <v-divider
      class="my-4"
    >
    </v-divider>
    <v-row
      align="center"
      no-gutters
    >
      <v-col>
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'cla_res1c';
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        class="shrink"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="() => {
            const expectedAnswers = [state.cla_low_age, state.cla_high_age];
            state.marker = validateAnswersJS(['low_age', 'high_age'], expectedAnswers) ? 'age_dis1c' : 'cla_age1c';
          }"
        >
          check
        </v-btn>
      </v-col>
    </v-row>
  </v-alert> 
</template>

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

<script>
export default = {

  methods: {
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
        this.failedValidationAgeRange = (value && value === expectedAnswers[index]) ? false : true;
        console.log("expectedAnswer", expectedAnswers);
        console.log("entered value", value);
        return value && value === expectedAnswers[index];
      });
    }
  }
};
</script>

