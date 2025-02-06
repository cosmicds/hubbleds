<template>
  <scaffold-alert
    title-text="Identify Your Confidence Interval"
    @back="back_callback()"
    @next="next_callback();"
    :can-advance="can_advance"
  >
    <template #before-next>
      Enter a response.
    </template>
    <div
      class="mb-4"
    >
      <p>
        After comparing the mean, median, and mode(s) of your class's age measurements within the histogram, enter your responses below.
      </p>
      <v-row>
        <v-col
          cols="12"
          lg="9">      
          1. The <b>most likely</b> age of the universe based on my class’s data set: 
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
                    Hint #1
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
            label="Most Likely Age"
            :tag="state_view.free_response_a.tag"
            type="float"
            :initial-response="state_view.free_response_a.response"
            :initialized="state_view.free_response_a.initialized"
            @fr-emit="(e) => {best_guess_answered = true;fr_callback(e);}"
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
        v-if="best_guess_answered"
      >
        <v-col>
          2. Explain why you picked that value and how your choice is connected to your understanding of the mean, median, or mode.
        </v-col>
      </v-row>
      <v-row
        v-if="best_guess_answered"
      >
        <v-col>
          <free-response
            outlined
            auto-grow
            rows="2"
            label="My Reasoning"
            :tag="state_view.free_response_b.tag"
            :initial-response="state_view.free_response_b.response"
            :initialized="state_view.free_response_b.initialized"
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
      best_guess_answered: false,
    }
  },
  mounted() {
    if (this.state_view.free_response_a.response != '' && !this.best_guess_answered) {
      this.best_guess_answered = true;
    }
  },
}
</script>

