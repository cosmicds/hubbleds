<template>
  <v-dialog
      v-model="dialog"
      max-width="1000px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="my-2"
        block
        color="secondary"
        elevation="2"
        id="uncertainty-button"
        @click.stop="() => { 
          dialog = true; 
          }"
      >
        Uncertainty Tutorial
      </v-btn>
    </template>
    <v-card
      class="mx-auto"
      ref="content"
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
          {{ titles[step] }}
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <!-- <speech-synthesizer
          :root="() => this.$refs.content.$el"
          :selectors="['div.v-toolbar__title', 'div.v-card__text.black--text', 'h3', 'p']"
          /> -->
        <v-btn
          icon
          @click="() => { 
            dialog = false;
            if (step === length-1) 
              { 
                on_slideshow_finished();
                step = 0;  
              }
          }"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

        <v-window
          v-model="step"
          style="height: 70vh;"
          class="overflow-auto"
        >

        <v-window-item :value="0" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row
              >
                <v-col 
                  cols="6"
                  style="align-content:center!important; justify-content:center!important" 
                >
                  <div class="ma-4">
                    <p>
                      There is only one universe that we live in, so our universe only has one age. Our job as scientists is to figure out if the <b>true age</b> of the universe is included within the ranges given by our measurements, and if so, which value within the range is the true age.
                    </p>
                    <p>
                      First, let’s think about <b>why</b> we found a range of values in the first place (rather than all getting the same value).
                    </p>
                  </div>
                </v-col>
                <v-col
                  cols="6"
                >
                  <div>
                    <v-img
                      class="mb-4 mx-a mt-n3 image-fit"
                      alt="Cartoon image of the Universe and a birthday cake with a question mark candle."
                      :src="`${image_location}/universecake.png`"
                    ></v-img>
                    <div>
                      <cite class="text-center mt-2 grey--text">
                        Students, classes, (and scientists) have measured different ages for our universe. How do we know which is the <b>true</b> age? Credit: Anna Nolin 
                      </cite>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>
        <v-window-item :value="1" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    If you recall, you identified these shortcomings in your measurements and your estimate of the universe's age.
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Shortcoming #1:
                  </p>
                  <p 
                    class = "StudentResponses">

                    {{ age_calc_short1 }}
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Shortcoming #2:
                  </p>
                  <p
                    class = "StudentResponses">

                    {{ age_calc_short2 }}
                  </p>
                  <p
                    class="mb-3 mt-10"
                  >
                    Other shortcomings:
                  </p>
                  <p
                    class = "StudentResponses">

                    {{ age_calc_short_other }}
                  </p>
                  <p class="mt-10">
                    Is there anything more you would like to add now that you’ve seen more data? (It’s OK if not.)
                  </p>
                  <free-response
                    outlined
                    auto-grow
                    rows="2"
                    label="Shortcoming #4"
                    hint="(if you can think of any more)"
                    tag="shortcoming-4"
                    :allow-empty="true"
                    :initial-response="free_responses[0]?.response"
                    :initialized="free_responses[0]?.initialized"
                    @fr-emit="fr_callback($event)"
                  ></free-response>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="2" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <p>
                    There are a few things that could prevent us from finding the true age of the universe:
                  </p>
                  <ul>
                    <li>Our <b>methods</b> are imperfect</li>
                    <li>Our <b>assumptions</b> about the universe are imperfect</li>
                    <li>Our <b>measurements</b> are imperfect</li>
                  </ul>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="3" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols = "12"
                >
                  <p>
                    Given the messiness of our velocity vs. distance graphs, it is clear that we did not use an optimal method for making these measurements.
                  </p>
                  <p>
                    In particular, professional astronomers have more sophisticated ways to measure <b>distances</b> to galaxies (but those are outside of the scope of this data story).
                  </p>
                  <p>
                    To make our measurements, we assumed that all galaxies are the same size as our own galaxy, the Milky Way. This is not a correct assumption, as galaxies have a large amount of natural variability in their sizes. This is likely the biggest source of “messiness” in our results.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="4" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  >
                  <p>
                    Human error also contributes to imperfect measurements. Some people are more meticulous than others.
                  </p>
                  <p>
                    Sometimes our tools limit our measurements. For example, did you feel confident that you were able to measure the edges of your galaxies correctly?
                  </p>
                  <p>
                    Given the imperfect nature of our measurements and assumptions, there is a chance that our results are different than the true age of the universe. We refer to these differences as <b>uncertainties</b> in our result.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="5" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  >
                  <p>
                    Some uncertainties are <b>random</b>. For example, if some galaxies in your sample are larger or smaller than the Milky Way, your resulting distances may be too close or too far, and then your resulting age may be too young or too old.
                  </p>
                  <p>
                    With <b>random</b> uncertainties, your measurements are as likely to be too high or too low, and with enough data, those variations would likely average out.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="6" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  cols="7"
                  >
                  <p>
                    Some uncertainties are <b>systematic</b>. These are problems with our methods or assumptions that lead to all measurements, on average, being <b>incorrect in the same direction</b>, which biases our final result.
                  </p>
                  <p>
                    For example, imagine using a wrinkled tape measure to determine lengths. All your measurements would read larger than they should.
                  </p>
                  <p>
                    Can you think of any problems in our methods that could bias everyone’s results in the same direction?
                  </p>
                  <free-response
                    outlined
                    auto-grow
                    rows="2"
                    label="Problems in Our Methods"
                    hint="(problems that might lead to systematic uncertainty)"
                    tag="systematic-uncertainty"
                    :initial-response="free_responses[1]?.response"
                    :initialized="free_responses[1]?.initialized"
                    @fr-emit="fr_callback($event)"
                  ></free-response>
                </v-col>
                <v-col
                  cols="5"
                >
                  <div>
                    <v-img
                      class="mb-4 mx-a mt-n3 image-fit"
                      alt="Two measuring tapes are side by side. One lies straight. The other is curled up and wrinkled."
                      :src="`${image_location}/rulers.png`"
                    ></v-img>
                    <div>
                      <cite class="text-center mt-2 grey--text">
                        Systematic errors can result from using flawed measuring tools or using tools incorrectly. Lengths measured with the wrinkled measuring tape will all be too long. Credit: Anna Nolin 
                      </cite>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="7" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col
                  >
                  <p>
                    Here are possible sources of systematic uncertainty:
                  </p>
                  <ul>
                    <li>
                      If we all miss measuring the faint outer edges of all our galaxies, our angular size measurements will all be a little bit too small, and everyone’s distance measurements will be a little bit too far, leading to ages that are a little bit too old.
                    </li>
                    <li>
                      We know that there is natural variation in the sizes of galaxies. If our Milky Way happens to be an “average” galaxy (somewhere in the middle of the actual distribution of galaxy sizes), our result would not have a bias. If the “average” size of a galaxy is different than the size of the Milky Way, that could lead to a bias in our age measurements.
                    </li>
                  </ul>
                  <br>
                  <p>
                    Sometimes sources of systematic uncertainty bias our results in different directions, effectively cancelling each other out in a lucky coincidence.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="8" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col> 
                  <p>
                    Scientists try to eliminate as many sources of systematic bias as possible designing an experiment. Figuring out and accounting for all possible sources of systematic uncertainty is one of the most difficult (and most important!) tasks in science. 
                  </p>
                  <p>  
                    Because our time is limited, from here on out, our exploration of uncertainties will focus only on <b>random</b> uncertainties.
                  </p>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="9" class="no-transition">
          <v-card-text>
            <v-container>
              <v-row>
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
                    You're ready to continue exploring the data now.
                  </h3>
                  <span class="text-caption grey--text">Click the <b>UNCERTAINTY TUTORIAL</b> button again if you'd like to come back for a refresher.</span>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-window-item>  
        
      </v-window> 
      <v-divider></v-divider>

      <v-card-actions
        class="justify-space-between"
      >
        <v-btn
          :disabled="step === 0"
          class="black--text"
          color="accent"
          depressed
          @click="set_step(step - 1);" 
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
            v-slot="{ active, toggle }"
          >
            <v-btn
              :disabled="n > max_step_completed + 2"
              :input-value="active"
              icon
              @click="toggle"
            >
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="disableNext"
          v-if="step < length-1"
          color="accent"
          class="black--text"
          depressed
          @click="set_step(step + 1);"
        >
          {{ step < length-1 ? 'next' : '' }}
        </v-btn>
        <v-btn
          v-if="step < length-1"
          class="demo-button"
          depressed
          @click="() => {
            $emit('close');
            dialog = false;
            set_step(0);
            on_slideshow_finished();
            // this.$refs.synth.stopSpeaking();
          }"
        >
          move on
        </v-btn>        
        <v-btn
          v-if = "step == length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { 
            dialog = false; 
            on_slideshow_finished();
            set_step(0);
          }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
module.exports = {
  data() {
    return {
      disableNext: false,
      freeResponses: [],
      frListener: null,
      listenerSetup: false,
    };
  },

  mounted() {
    const root = this.getRoot();
    this.setupObserver();
  },

  methods: {
    getRoot() {
      return this.$refs.content.$el;
    },
    setupObserver() {
      if (this.listenerSetup) {
        return;
      }
      const root = this.getRoot();
      this.frObserver = new MutationObserver((mutations) => {
        let needUpdate = false;
        mutations.forEach(mutation => {
          if (needUpdate) {
            return;
          }
          if (mutation.addedNodes.length > 0) {
            needUpdate = [...mutation.addedNodes].some(this.needUpdateNode);
          }
          if (!needUpdate && mutation.removedNodes.length > 0) {
            needUpdate = [...mutation.removedNodes].some(this.needUpdateNode);
          }
        });
        if (needUpdate) {
          this.updateFreeResponseList();
          this.updateDisableNext();
        }
      });
      this.frObserver.observe(root, { childList: true, subtree: true });
      this.listenerSetup = true;
    },
    // These methods are kinda hacky!
    // but they let us not ever have to deal with this stuff elsewhere
    // and not have to rewrite this in each guideline that has free responses
    updateFreeResponseList() {
      const root = this.getRoot();
      const frElements = root.querySelectorAll(".cds-free-response");
      const frComponents = [...frElements].map(fr => fr.__vue__);
      for (let i = 0; i < frComponents.length; i++) {
        if (frComponents[i].$vnode.tag.indexOf("FreeResponse") < 0) {
          frComponents[i] = frComponents[i].$parent;
        }
      }
      this.freeResponses = frComponents;

      if (this.freeResponses.length > 0 && this.frListener === null) {
        this.frListener = (_event) => {
          this.updateDisableNext();
        };
        root.addEventListener('input', this.frListener);
      }
    },

    allFreeResponsesFilled() {
      return this.freeResponses.every(fr => fr.$refs.textarea.valid);
    },

    updateDisableNext() {
      this.disableNext = this.require_fr && !this.allFreeResponsesFilled();
    },

    needUpdateNode(node) {
      return node.classList != undefined &&
        (
          node.classList.contains("cds-free-response")
            ||
          node.querySelectorAll(".cds-free-response").length > 0
        );
    }
  },

  watch: {
    step(newStep, oldStep) {
      const isInteractStep = this.freeResponses.length > 0;
      this.set_step(newStep);
      this.set_max_step_completed(Math.max(this.max_step_completed, newStep - 1));
    },
    dialog(value) {
      if (value) {
        this.$nextTick(() => {
          this.setupObserver();
        });
      }
    }
  }
}
</script>
