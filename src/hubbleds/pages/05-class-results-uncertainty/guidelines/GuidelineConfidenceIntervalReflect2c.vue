<!-- this state_view.marker = con_int2c -->
<template>
  <scaffold-alert
    title-text="Identify Your Confidence Interval"
    @back="back_callback()"
    @next="next_callback()"
    :can-advance="can_advance"
  >
    <template #before-next>
      Enter responses.
    </template>
    <div
      class="mb-4"
    >
      <p>
        From your class's data, you determined that the most likely value for the age of the universe was: <StudentResponse class="StudentResponses">{{ state_view.best_guess }}</StudentResponse>&nbsp;Gyr, with a confidence interval from <StudentResponse class="StudentResponses">{{ state_view.low_guess }}</StudentResponse>&nbsp;to <StudentResponse class="StudentResponses">{{ state_view.high_guess }}</StudentResponse>&nbsp;Gyr.
      </p>
      <p>
        Update your responses based on the additional data from this larger All Classes data set.
      </p>
      <v-row>
        <v-col
          cols="12"
          lg="9">      
          1. My new most likely value for the age of the universe based on the data set from All Classes: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="dialog1 = true"
          >
            hint
            <v-dialog
              v-model="dialog1"
              max-width="600px">
              <v-card
                class="mx-auto"
              >
                <v-toolbar
                  color="secondary"
                  dense
                  dark
                >
                  <v-toolbar-title
                    class="text-h6 text-uppercase font-weight-regular"
                    style="color: white;"
                  >
                    Hint #1
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        dialog1 = false;
                      }
                    "
                  >
                    <v-btn icon>
                      <v-icon> mdi-close </v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div class="pa-6">
                  <p>
                    Sometimes, the mean, median, and mode of a distribution all have the same value. That value would be a strong candidate for being the most likely value based on the distribution.
                  </p>
                  <p>
                    When the values do not agree, you can choose any of the mean, median or mode, or even something different, as long as you justify why you chose it. You can review what each quantity represents and when scientists might use it by clicking the <v-icon>mdi-help-circle-outline</v-icon> next to it.
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="11"
          lg="3"
        >
          <free-response
            outlined
            rows="1"
            label="New Most Likely Age"
            :tag="state_view.free_response_a.tag"
            type="float"
            :initial-response="state_view.free_response_a.response"
            :initialized="state_view.free_response_a.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
        <v-col
          class="fr-unit-custom"
          cols="1"
          lg="2">
          Gyr<p>&nbsp;</p>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          lg="9"
        >
          2. The new range of age values for the universe that I am most confident in based on the data set from All Classes: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="dialog2 = true"
          >
            hint
            <v-dialog
              v-model="dialog2"
              max-width="600px">
              <v-card
                class="mx-auto"
              >
                <v-toolbar
                  color="secondary"
                  dense
                  dark
                >
                  <v-toolbar-title
                    class="text-h6 text-uppercase font-weight-regular"
                    style="color: white;"
                  >
                    Hint #2
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        dialog2 = false;
                      }
                    "
                  >
                    <v-btn icon>
                      <v-icon> mdi-close </v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div class="pa-6">
                  <p>
                    The range you pick will have a tradeoff between how likely it is that the “true” value actually lies within the range you choose vs. having a narrow enough range that your measurement is actually useful. A very large range is more likely to include the "true" value, but may be so nonspecific that it is not useful. A narrow range has more specificity but may not include the "true" value.
                  </p>
                  <p>
                    Different people will feel more or less comfortable with the different sides of this tradeoff, and there isn’t really a right or wrong answer as long as you justify why you
                    chose what you did.
                  </p>
                  <p>
                    If you are feeling really stuck, feel free to discuss this with a classmate or your instructor.
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="11"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="New Likely Low Age"
            :tag="state_view.free_response_b.tag"
            type="float"
            :initial-response="state_view.free_response_b.response"
            :initialized="state_view.free_response_b.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
        <v-col
          class="fr-unit-custom"
          cols="1"
          lg="2">
          Gyr<p>&nbsp;</p>
        </v-col>
              <v-col
          cols="11"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="New Likely High Age"
            :tag="state_view.free_response_c.tag"
            type="float"
            :initial-response="state_view.free_response_c.response"
            :initialized="state_view.free_response_c.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
        <v-col
          class="fr-unit-custom"
          cols="1"
          lg="2">
          Gyr<p>&nbsp;</p>
        </v-col>
      </v-row>

      <p class="mt-4">
        3. Explain why you chose these new values based on the All Classes data:
      </p>
      <free-response
        outlined
        rows="1"
        label="My Updated Reasoning"
        :tag="state_view.free_response_d.tag"
        :initial-response="state_view.free_response_d.response"
        :initialized="state_view.free_response_d.initialized"
        @fr-emit="fr_callback($event)"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
<script>
export default {
  data() {
    return {
      dialog1: false,
      dialog2: false,
    }
  },
}
</script>
