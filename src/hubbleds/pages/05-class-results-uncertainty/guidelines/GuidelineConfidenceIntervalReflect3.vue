<template>
  <scaffold-alert
    title-text="Identify Your Confidence Interval"
    ref="scaffold"
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
        After comparing different percentage ranges for your class's age measurements in the histogram, enter your responses below.
      </p>
      <v-row
      >
        <v-col
          cols="12"
          lg="9"
        >
          3. The range of age values for the universe that I am most confident in based on my class’s data set: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="dialog = true"
          >
            hint
            <v-dialog
              v-model="dialog"
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
                        dialog = false;
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
                    Different people will feel more or less comfortable with the different sides of this tradeoff, and there isn’t really a right or wrong answer as long as you justify why you chose what you did.
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
        <v-row>
        <v-col
          cols="11"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="Likely Low Age"
            :tag="state_view.free_response_a.tag"
            type="float"
            :initial-response="state_view.free_response_a.response"
            :initialized="state_view.free_response_a.initialized"
            @fr-emit="(e) => {likely_low_answered = true; fr_callback(e)}"
          ></free-response>
        </v-col>
        <v-col
          class="fr-unit-custom"
          cols="1"
          lg="2">
          Gyr<p>&nbsp;</p>
        </v-col>
        </v-row>
              <v-col
          cols="11"
          lg="3">
          <free-response
            outlined
            rows="1"
            label="Likely High Age"
            :tag="state_view.free_response_b.tag"
            type="float"
            :initial-response="state_view.free_response_b.response"
            :initialized="state_view.free_response_b.initialized"
            @fr-emit="(e) => {likely_high_answered = true; fr_callback(e)}"
          ></free-response>
        </v-col>
        <v-col
          class="fr-unit-custom"
          cols="1"
          lg="2">
          Gyr<p>&nbsp;</p>
        </v-col>
      </v-row>

      <v-row
        v-if="high_low_answered"
      >
        <v-col>
          4. Explain why you chose your values using information from the histogram or other viewers:
        </v-col>
      </v-row>
      <v-row
        v-if="high_low_answered"
      >
        <v-col>
          <free-response
            outlined
            auto-grow
            rows="2"
            label="My Reasoning"
            :tag="state_view.free_response_c.tag"
            :initial-response="state_view.free_response_c.response"
            :initialized="state_view.free_response_c.initialized"
            @fr-emit="fr_callback($event)"
          ></free-response>
        </v-col>
      </v-row>


    </div>
  </scaffold-alert>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      likely_low_answered: false,
      likely_high_answered: false,
    }
  },
  computed: {
    high_low_answered() {
      return this.likely_low_answered && this.likely_high_answered;
    }
  }
}
</script>

