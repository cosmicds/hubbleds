<template>
  <v-dialog
      v-model="dialog"
      max-width="800px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        block
        color="warning"
        elevation="2"
        @click.stop="set_dialog(true)"
      >
        <v-spacer></v-spacer>
        Reflect
        <v-spacer></v-spacer>
        <v-icon
          class="ml-4"
        >
          {{ reflection_complete ? 'mdi-check-circle-outline' : 'mdi-circle-outline' }}
        </v-icon>
      </v-btn>
    </template>
    <v-card
      class="mx-auto"
      ref="content"
    >
      <v-toolbar
        color="warning"
        dense
        dark
      >
        <v-toolbar-title
          class="text-h6 text-uppercase font-weight-regular"
          style="color: white;"
        >
          {{ titles[step] }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <!-- <speech-synthesizer
          :root="() => this.$refs.content.$el"
          :autospeak-on-change="step"
          :speak-flag="dialog"
          :selectors="['label > div', 'div.v-toolbar__title', 'div.v-card__text.black--text', 'h3', 'p']"
        >
        </speech-synthesizer> -->
        <span>
          <v-btn
            icon
            @click="() => { 
            dialog = set_dialog(false);
            if (step === length-1) 
              { 
                on_reflection_complete();
                set_step(0);  
              }
            }"
          >
            <v-icon> mdi-close </v-icon>
          </v-btn>
        </span>
      </v-toolbar>

      <v-window
        v-model="step"
        vertical
        style="height: 60vh;"
        class="overflow-auto"
      >
        <v-window-item :value="0"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    Throughout this reflection sequence, you will answer questions that are designed to guide your thinking. Your responses will be recorded (as in a scientist’s lab notebook), so that you can use this information to support your claims later in this Data Story.
                  </p>
                  <p>
                    Scientists do not work in a vacuum and neither should you. You can consult colleagues (i.e. classmates or lab partners) and instructors for help.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="1"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="7"
                >
                  <p>
                    Recall that you are looking at the same kind of observations Vesto Slipher made in the 1910s-1920s. We’ll ask you some questions about your data that astronomers in 1920 might have asked about Slipher’s data.
                  </p>
                </v-col>
                <v-col
                  cols="5"
                >
                  <div>
                    <v-img
                      class="mb-4 mx-a mt-n3 image-fit"
                      alt="A black and white image of the Andromeda galaxy's light spectrum"
                      src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_one_spectrum/vesto_slipher.png"
                    ></v-img>
                    <div>
                      <cite class="text-center mt-2 grey--text">
                        Vesto Slipher's spectrum of the Andromeda Galaxy  from Lowell Observatory
                        <span style="display: none">
                          Source: Modified from <a href="https://ui.adsabs.harvard.edu/abs/2009JAHH...12...72B/abstract">Br&eacture;mond, Journal of Astronomical History and Heritage, 2009</a>
                        </span>
                      </cite>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="2"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    How do the observed wavelengths of your galaxies' spectral lines compare with their rest wavelengths?
                  </p>
                  <p>
                    Choose the best response below.
                  </p>
                  <p>
                    <b>Note: If this window is in the way of your data table, click the header and drag it to a different part of the screen.</b>
                  </p>
                  <mc-radiogroup
                    :radio-options="[
                      'In ALL of my galaxies, the observed wavelengths of the spectral lines are the SAME as the rest wavelengths.',
                      'In ALL of my galaxies, the observed wavelengths of the spectral lines are LONGER than the rest wavelengths.',
                      'In ALL of my galaxies, the observed wavelengths of the spectral lines are SHORTER than the rest wavelengths.',
                      'In SOME of my galaxies, the observed wavelengths of the spectral lines are LONGER than the rest wavelengths. In OTHER of my galaxies, the observed wavelengths of the spectral lines are SHORTER than the rest wavelengths.'
                    ]"
                    :feedbacks="[
                      'That is an unexpected result. For each galaxy, compare the values for rest wavelength (column 3) and observed wavelength (column 4). Check with an instructor in case your measurements need adjustment.',
                      'That is interesting that the observed spectral lines are all longer than the rest wavelengths.',
                      'That is an unexpected result. For each galaxy, compare the values for rest wavelength (column 3) and observed wavelength (column 4). Check with an instructor in case your measurements need adjustment.',
                      'That is an unexpected result. For each galaxy, compare the values for rest wavelength (column 3) and observed wavelength (column 4). Check with an instructor in case your measurements need adjustment.'
                    ]"
                    :correct-answers="[1]"
                    @select="(option) => { if(option.correct) { set_max_step_completed(Math.max(max_step_completed, 2)); } }"
                    @mc-emit="mc_callback($event)"
                    :score-tag="state_view.score_tag_2"
                    :initialization="state_view.mc_score_2"
                  >
                  </mc-radiogroup>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="3"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    From the data you have collected so far, what can you conclude about how your observed galaxies are moving relative to our home galaxy, the Milky Way?
                  </p>
                  <p>
                    Choose the best response below.
                  </p>
                  <mc-radiogroup
                    :radio-options="[
                      'My observed galaxies are NOT moving relative to our galaxy.',
                      'All of my observed galaxies are moving AWAY from our galaxy.',
                      'All of my observed galaxies are moving TOWARD our galaxy.',
                      'Some of my observed galaxies are moving AWAY from our galaxy, and some galaxies are moving TOWARD our galaxy.'
                    ]"
                    :feedbacks="[
                      'Try again. Recall that when the observed wavelength is LONGER than the rest wavelength, this indicates motion AWAY from the observer.',
                      'That is correct.',
                      'Try again. Recall that when the observed wavelength is LONGER than the rest wavelength, this indicates motion AWAY from the observer.',
                      'Try again. Recall that when the observed wavelength is LONGER than the rest wavelength, this indicates motion AWAY from the observer.'
                    ]"
                    :correct-answers="[1]"
                    @select="(option) => { if(option.correct) { set_max_step_completed(Math.max(max_step_completed, 3)); } }"
                    @mc-emit="mc_callback($event)"
                    :score-tag="state_view.score_tag_3"
                    :initialization="state_view.mc_score_3"
                  >
                  </mc-radiogroup>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="4"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    You concluded from your data that all five of your galaxies seem to be <strong>moving away</strong> from our Milky Way galaxy.
                  </p>
                  <p>
                    Remember that the dominant view in the 1920’s is that the universe is <strong>static</strong> and <strong>unchanging</strong>. Are your data consistent with this model of the universe?
                  </p>
                  <mc-radiogroup
                    :radio-options="[
                      'Yes.',
                      'No.',
                      'I am not sure.'
                    ]"
                    :feedbacks="[
                      'Actually, your evidence does not support this statement. Galaxies would not be moving in a universe that is static and unchanging.',
                      'That\'s right. In a static, unchanging universe, galaxies would not be moving like yours are.',
                      'You <strong>can</strong> draw a conclusion about this statement based on your evidence. Consider this and try again: galaxies would not be moving in a universe that is static and unchanging. And you have already concluded that your observed galaxies are moving. So...'
                    ]"
                    :correct-answers="[1]"
                    :neutral-answers="[2]"
                    @select="(option) => { if(option.correct || option.neutral) { set_max_step_completed(Math.max(max_step_completed, 4)); } }"
                    @mc-emit="mc_callback($event)"
                    :score-tag="state_view.score_tag_4"
                    :initialization="state_view.mc_score_4"
                  >
                  </mc-radiogroup>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="5"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    An alternate hypothesis of the 1920's is that galaxies in the universe are <strong>moving randomly</strong>.
                  </p>
                  <p>
                    Are your data consistent with this model of the universe?
                  </p>
                  <mc-radiogroup
                    :radio-options="[
                      'Yes.',
                      'No.',
                      'I am not sure.'
                    ]"
                    :feedbacks="[
                      'With only 5 galaxies, it is difficult to draw strong conclusions about the motion of galaxies. However, note that your galaxies all seem to be moving in the same direction (away from us). If galaxies move randomly, you would expect some to be moving toward us and some to be moving away.',
                      'Your galaxies all seem to be moving in the same direction (away from us), which is NOT consistent with galaxies that move randomly. However, it may be difficult to say for sure with data from only 5 galaxies.',
                      'That\'s fair. With only 5 galaxies, it is difficult to draw strong conclusions about the motion of galaxies. However, note that your galaxies all seem to be moving in the same direction (away from us). If galaxies move randomly, you would expect some to be moving toward us and some to be moving away.'
                    ]"
                    :neutral-answers='[0,1,2]'
                    @select="(option) => { if(option.neutral) { set_max_step_completed(Math.max(max_step_completed, 5)); } }"
                    @mc-emit="mc_callback($event)"
                    :score-tag="state_view.score_tag_5"
                    :initialization="state_view.mc_score_5"
                  >
                  </mc-radiogroup>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="6"
          class="no-transition"
        >
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    You have looked at the spectra for only 5 galaxies. It might give you more confidence if you pool your data with others, so that you can draw conclusions from a larger number of galaxies.
                  </p>
                  <p>
                    Take a minute to talk with your peers. Do their data agree or disagree with yours?
                  </p>
                  <mc-radiogroup
                    :radio-options="[
                      'Their data agree with mine. Their galaxies are also moving away from us.',
                      'Their data disagree with mine. Their galaxies are not all moving away from us.',
                      'I am working on my own and do not have someone to check with.'
                    ]"
                    :feedbacks="[
                      'Interesting that they also got the same result as you. Does that give you more confidence in your conclusions?',
                      'Hmm. That is an unexpected result. It might be helpful to check in with your instructor.',
                      'No problem. Checking the Cosmic Data Stories database, everyone else who has completed this story also found that their galaxies are all moving away from us. Does that give you more confidence in your conclusions?']"
                    :correct-answers="[0,2]"
                    :neutral-answers="[1]"
                    @select="(option) => { if(option.correct || option.neutral) { set_max_step_completed(Math.max(max_step_completed, 6)); } }"
                    @mc-emit="mc_callback($event)"
                    :score-tag="state_view.score_tag_6"
                    :initialization="state_view.mc_score_6"
                  >
                  </mc-radiogroup>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>


        <v-window-item :value="7"
          class="no-transition"
          style="height: 100%;"
        >
          <v-card-text
            style="height: 100%;"
          >
            <v-container
              style="height: 100%;"
            >
              <v-row
                style="height: 100%;"
                align="center"
              >
                <v-col
                  class="pa-4 text-center my-auto"
                >
                  <v-img
                    class="mb-4"
                    contain
                    height="128"
                    src="https://www.pngrepo.com/png/211744/512/rocket-ship-launch-missile.png"
                  ></v-img>
                  <h3 class="text-h6 font-weight-light mb-2">
                    Nice work reflecting!
                  </h3>
                  <span class="text-caption grey--text">You can start calculating velocities now.</span>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn
          :disabled="step === 0"
          class="black--text"
          color="accent"
          depressed
          @click="set_step(step - 1)"
        >
          Back
        </v-btn>
        <v-spacer></v-spacer>
        <v-item-group
          v-model="step"
          class="text-center"
          mandatory
        >
          <v-item
            v-for="n in length"
            :key="`btn-${n}`"
            v-slot="{ active }"
          >
          <!-- vue's v-for with a range starts the count at 1, so we have to add 2 in the disabled step instead of 1 to account for the fact that we are otherwise counting the windows from 0 https://v2.vuejs.org/v2/guide/list.html?redirect=true#v-for-with-a-Range-->
            <v-btn
              :disabled="require_responses && n > max_step_completed + 2"
              :input-value="active"
              icon
              @click="set_step(n-1);"
            >
              <v-icon
                color="info"
              >
                mdi-record
              </v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-spacer></v-spacer>
        <v-btn
          v-if="step < length-1"
          :disabled="require_responses && step > max_step_completed"
          class="black--text"
          color="accent"
          depressed
          @click="set_step(step + 1)"
        >
          Next
        </v-btn>
        <v-btn
          v-if="step < length-1"
          class="demo-button"
          depressed
          @click="() => {
            set_dialog(false);
            on_reflection_complete();
            set_step(0); 
            // this.$refs.synth.stopSpeaking();
          }"
        >
          move on
        </v-btn>    
        <v-btn
          v-if="step === length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { 
            set_dialog(false);
            on_reflection_complete();
            set_step(0); 
          }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<style>
.no-transition {
  transition: none;
}
</style>


<script>
module.exports = {

  watch: {
    step(newStep, oldStep) {
        const isInteractStep = this.interact_steps.includes(newStep);
        const newCompleted = isInteractStep ? newStep - 1 : newStep;
        this.set_max_step_completed(Math.max(this.max_step_completed, newCompleted));
    }
  }
};
</script>
