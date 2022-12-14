<template>
  <v-card
    id="slideshow-root"
    elevation="6"
  >
    <v-toolbar
      color="info"
      dense
      dark
    >
      <v-toolbar-title
        class="text-h6 text-uppercase font-weight-regular"
      >
        {{ currentTitle }}
      </v-toolbar-title>
    </v-toolbar>

    <v-window
      style="min-height: 300px;"
      v-model="step"
    >
      <v-window-item :value="0" 
        class="no-transition"
      >
        <v-card-text
          style="min-height: 550px;"
        >
          <v-container>
            <v-row
              no-gutter
            >
              <v-col cols="6">
                <p>
                  Welcome to the <b><i>Hubble's Law</i> Cosmic Data Story</b> where you will use real astronomical data&#8212;old and new&#8212;to investigate the mysteries of our Universe. In particular, let's ask:
                </p>
                <v-card
                  class="justify-center pa-2 mx-12 my-8"
                  color="primary lighten-1"
                  style="font-weight:600;"
                  dark
                >
                  <p
                    class="my-3 text-center"
                  >
                    Has the universe always existed?
                  </p>
                  <p
                    class="my-3 text-center"
                  >
                    If not, how long ago did it form?
                  </p>
                </v-card>
                <p>
                  When scientists collect data to answer questions no one has answered yet, there is no answer key in the back of some book. So, as you explore this data story, you will learn how to <b>evaluate the reliability</b> of your results. Are the data really good enough to support a conclusion? <b>How can you know?</b> 
                </p>
                <p>
                  Just as scientists constantly must, you'll <b>determine what can be concluded</b> from the data at-hand, and <b>how much confidence</b> you can have in your conclusions.
                </p>
                <p>
                  Let's get started.
                </p>
              </v-col>
              <v-col cols="6">
                <v-img
                  lazy-src="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
                  src="https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
                  alt="Hubble Telescope"
                ></v-img>
                <div
                  class="text-center mt-2 grey--text"
                  style="width: 100%;"
                >
                  <i>Ever wonder who the Hubble Space Telescope is named for, and why?</i>
                </div>
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
              <v-col cols="6">
                <p>
                  Imagine that you are an astronomer living in the <b>early 1920s</b>. You and your colleagues around the world, including Albert Einstein, would agree that the <b>universe is unchanging</b> and <b>everlasting.</b> In other words, you expect that the universe always has been and will be the way it is the way you see it now. This picture of an unchanging universe had rarely been questioned throughout human history, thanks in large part to <b>Aristotle</b>, who embraced perfection and permanence. 
                </p>
                </v-col>
                <v-col cols="6">
                <v-img
                  lazy-src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/School_of_Athens.jpg"
                  src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/School_of_Athens.jpg"
                  alt="School of Athens"
                ></v-img>
                <div
                  class="text-center mt-2 grey--text"
                  style="width: 100%;"
                >
                  <i>Plato (red robe) and his pupil Aristotle (blue robe) at the center of ???The School of Athens,??? painted by Raphael for the walls of the Vatican between 1509 and 1511. Aristotle lived from 384-322 BC, and his theory of an unchanging universe persisted until the time of Edwin Hubble, 23 centuries later. </i>
                </div>
              </v-col>
                </p>
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
                <div
                  style="min-height: 120px;"
                >
                  <p>
                    The frame below provides an <b>interactive view </b>of the night sky, using images from real observations.
                  </p>
                  <p>
                    The brighter band you see going diagonally across the frame (before you try the controls) is caused by stars and dust in our home galaxy, called the <b>Milky Way.</b>
                  </p>
                  <p>
                    You can explore this view and see what is in the night sky, as astronomers have been doing for centuries. <b>Pan</b> (click and drag) and <b>zoom</b> (scroll in and out) to see parts of the sky beyond this view.
                </div>
                <div
                  class="mb-2 mx-4"
                >    
                  <v-row>
                    <v-col
                      cols="8"
                      offset-lg="1"
                    > 
                      <c-exploration-tool id="exploration-tool">
                    </v-col>
                    <v-col
                      cols="4"
                      lg="3"
                    >
                      <v-row>
                        <v-col
                          cols="12"
                          lg="4"
                        >
                          <v-chip
                            label
                            outlined
                          >
                            Pan
                          </v-chip>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="8"
                          class="pt-2"
                        >
                          <strong>click + drag</strong><br>
                          (or use <strong class="codeFont">I-J-K-L</strong> keys)
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col
                          cols="12"
                          lg="4"
                        >
                          <v-chip
                            label
                            outlined
                          >
                            Zoom
                          </v-chip>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="8"
                          class="pt-2"
                        >
                          <strong>scroll in and out</strong><br>
                          (or use <strong class="codeFont">Z-X</strong> keys)
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <div
                      class="text-center grey--text"
                      style="width: 100%;"
                    >
                      <i>Interactive view provided by WorldWide Telescope</i>
                    </div>
                  </v-row>
                </div>
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
                <div
                  style="min-height: 120px;"
                >
                  <p>
                    As you explore the cosmic sky, you may see stars and fuzzy blobs called <b>nebulae</b>. In the 1700's, French astronomer Charles Messier cataloged as many nebulae as he could find. They are known as Messier Objects and are identified by their catalog number. For example, M13 represents the 13th Messier Object in the catalog.
                  </p>
                  <p>
                    Click on the buttons to the right to <b>view some Messier Objects</b>. (Fun fact: ???nebula??? means ???cloud??? or ???fog??? in Latin.)
                  </p>
                </div>
                <div
                  class="mb-2 mx-4"
                >    
                  <v-row>
                    <v-col
                      cols="8"
                      offset-lg="1"
                    >   
                      <c-exploration-tool1 id="exploration-tool1">
                    </v-col>
                    <v-col
                      cols="4"
                      lg="2"
                    >
                      <v-row
                        justify="space-between"
                      >
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn 
                            @click="go_to_location_tool1({
                                ra: 83.63,
                                dec: 22.014,
                                fov: 350, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M1' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M1'"
                          >
                            M1 
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool1({
                                ra: 250.4,
                                dec: 36.46,
                                fov: 700, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M13' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M13'"
                          >
                            M13
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool1({
                                ra: 10.63,
                                dec: 41.27,
                                fov: 6000, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M31' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M31'"
                          >
                            M31 
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool1({
                                ra: 83.82,
                                dec: -5.39,
                                fov:7500, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M42' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M42'"
                          >
                            M42
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool1({
                                ra: 202.47,
                                dec: 47.195,
                                fov: 700, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M51' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M51'"
                          >
                            M51
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool1({
                                ra: 148.97,
                                dec: 69.68,
                                fov: 400, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M82' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M82'"
                          >
                            M82
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <div
                      class="text-center grey--text"
                      style="width: 100%;"
                    >
                      <i>Interactive view provided by WorldWide Telescope</i>
                    </div>
                  </v-row>
                </div>
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
                <div
                  style="min-height: 120px;"
                >
                  <p>
                    <b>M31</b> and <b>M51</b> are examples of a particular type of nebula that interested astronomers in the early 1900s. They were known as <b>spiral nebulae</b> because of their distinctive spiral shape. In 1920, there was a Great Debate between astronomers Harlow Shapley and Heber Curtis questioning whether the spiral nebulae were perhaps young solar systems being born within our Milky Way galaxy or were "island universes??? beyond it.
                  </p>
                  <p>
                    While you view these spiral nebulae, ponder what you would need to know to determine if they are within the Milky Way or beyond it. (Don't worry if you don't know. You will learn in this Data Story.) 
                  </p>
                </div>
                <div
                  class="mb-2 mx-4"
                >    
                  <v-row>
                    <v-col
                      cols="8"
                      offset-lg="1"
                    >
                      <c-exploration-tool2 id="exploration-tool2">
                    </v-col>
                    <v-col
                      cols="4"
                      lg="2"
                    >
                      <v-row
                        justify="space-between"
                      >
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            :disabled=true
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M1'"
                          >
                            M1
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            :disabled=true
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M13'"
                          >
                            M13
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool2({
                                ra: 10.63,
                                dec: 41.27,
                                fov: 6000, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M31' // name of object
                              })"

                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M31'"
                          >
                            M31
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            :disabled=true
                            color="info"
                            width="100%"
                            class="mx-2"
                          >
                            M42
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            @click="go_to_location_tool2({
                                ra: 202.47,
                                dec: 47.195,
                                fov: 700, // optional, in arcseconds, default is 90
                                instant: false, // also optional, false by default
                                target: 'M51' // name of object
                              })"
                            color="info"
                            width="100%"
                            class="mx-2"
                            :outlined="target === 'M51'"
                          >
                            M51
                          </v-btn>
                        </v-col>
                        <v-col
                          cols="12"
                          lg="6"
                        >
                          <v-btn
                            color="info"
                            width="100%"
                            class="mx-2"
                            :disabled=true
                          >
                            M82
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <div
                      class="text-center grey--text"
                      style="width: 100%;"
                    >
                      <i>Interactive view provided by WorldWide Telescope</i>
                    </div>
                  </v-row> 
                </div>
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
                  Between 1907&#8211;1921, Harvard astronomer <b>Henrietta Leavitt</b> observed Cepheid variable stars in a nebula called the Small Magellanic Cloud (SMC). By analyzing changes in the Cepheid stars??? brightness over time, she discovered that <b>fainter Cepheids vary more slowly than brighter ones</b>, as shown in her graph below. This important discovery made it possible to determine distances to spiral nebulae and finally resolve the Shapley-Curtis Great Debate: it turned out that spiral nebulae are far beyond the Milky Way and constitute <b>individual galaxies</b> in their own right.
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols= "8">
                <v-row>
                  <v-img
                      lazy-src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/Leavitt_at_work.jpg"
                      src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/Leavitt_at_work.jpg"
                      alt="Leavitt at Work "
                      max-height = "350"
                      contain
                    ></v-img>
                  <div
                    class="text-center mt-3 grey--text"
                    style="width: 100%;"
                  >
                    <i> Astronomer Henrietta Swan Leavitt </i>
                  </div>
                </v-row>
              </v-col>
              <v-col cols= "4">
                <v-row>
                  <v-img
                      lazy-src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/Leavitt_Plate.png"
                      src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/Leavitt_Plate.png"
                      alt="Leavitt Plate"
                      max-height = "200"
                      contain
                    ></v-img>
                  <div
                    class="text-center mb-6 mt-2 grey--text"
                    style="width: 100%;"
                  >
                    <i> Glass plate showing Cepheid variable stars in SMC studied by Leavitt</i>
                  </div>
                </v-row>
                <v-row>
                  <v-img
                      lazy-src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/HSLeavittHSCr13Fig2_1912.jpeg"
                      src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/HSLeavittHSCr13Fig2_1912.jpeg"
                      alt="Leavitt graph"
                      max-height = "200"
                      contain
                  ></v-img>
                  <div
                    class="text-center mt-3 grey--text"
                    style="width: 100%;"
                  >
                    <i>Graph from Leavitt's 1912 paper showing the relationship between period and brightness of Cepheid variables.</i>
                  </div>
                </v-row>
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
                  Around this same time, astronomer <b>Vesto Slipher</b> observed spiral nebulae using a spectrograph. Spectrographs can reveal a lot about an object in space, like what the object is made of or how fast it is moving toward or away from the observer.
                </p>
                <p>
                  Recall that the prevailing view in the early 1900s was that the universe is unchanging and eternal. As a result, the dominant expectation was that distant spiral nebulae are either not moving at all, or if they are moving then they are moving randomly.
                </p>
                <p>
                  It???s time for you to collect some of your own data, form conclusions, and compare your conclusions to what Vesto Slipher found.
                </p>
              </v-col>
              <v-col cols="5">
                <v-img
                  lazy-src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/V.M.Slipher.gif"
                  src="https://raw.githubusercontent.com/cosmicds/cds-website/main/public/hubbleds_images/stage_intro/V.M.Slipher.gif"
                  alt="Vesto Slipher"
                  max-height = "400"
                  contain
                ></v-img>
                  <div
                    class="text-center mt-3 grey--text"
                    style="width: 100%;"
                  >
                    <i>Astronomer Vesto Slipher</i>
                  </div>
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
        @click="() => {
          step--;
          if(step==3) go_to_location_tool1({ // reset viewer to MW
                                ra: 266.64, // default MW coords
                                dec: -28.39,
                                fov: 216000, // 60 degrees
                                instant: true, // also optional, false by default
                              })
          if(step==4) go_to_location_tool2({ // Set to M31 with button pressed
                                ra: 10.63,
                                dec: 41.27,
                                fov: 6000, // optional, in arcseconds, default is 90
                                instant: true, // also optional, false by default
                                target: 'M31' // name of object
                              })
          }"
      >
        back
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
            :input-value="active"
            icon
            @click="toggle"
          >
            <v-icon
              color="info lighten-1"
            >
              mdi-record
            </v-icon>
          </v-btn>
        </v-item>
      </v-item-group>
      <v-spacer></v-spacer>
      <!-- Code to use for disable in button below if step 2 depends on exploring WWT first: -->
      <!-- :disabled="step === 6 || (step === 2 && !exploration_complete)" -->
      <v-btn
        :disabled="step >= 6"
        v-if="step < 6"
        class="black--text"
        color="accent"
        depressed
        @click="() => {
          step++;
          if(step==3) go_to_location_tool1({ // reset viewer to MW
                                ra: 266.64, // default MW coords
                                dec: -28.39,
                                fov: 216000, // 60 degrees
                                instant: true, // also optional, false by default
                              })
          if(step==4) go_to_location_tool2({ // Go to M31 with button pressed
                                ra: 10.63,
                                dec: 41.27,
                                fov: 6000, // optional, in arcseconds, default is 90
                                instant: true, // also optional, false by default
                                target: 'M31' // name of object
                              })
          }"
      >
        next
      </v-btn>
      <!-- first button below just being used for testing, delete when using live with students -->
      <v-btn
        v-if="step < 6 && show_team_interface"
        color="error"
        class="black--text"
        depressed
        @click="() => {
          intro_complete = true;
          step = 0;
        }"
      >
        get started
      </v-btn>
      <v-btn
        v-if="step >= 6"
        :disabled="step > 6"
        color="accent"
        class="black--text"
        depressed
        @click="() => { 
          intro_complete = true;
          step = 0;
        }"
      >
        get started
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<style>
.no-transition {
  transition: none !important;
}

#slideshow-root .v-card__text{
  padding: 0px 15px 0px;
  min-height: 550px;
}

#exploration-tool, #exploration-tool2, #exploration-tool3 {
  height: 400px;
}


</style>


<script>
module.exports = {
  props: ["continueText","target"],

  watch: {
    step(val) {
      this.target = '';
    }
  }
};
</script>

<style>

div {
  color: "purple";
}

</style>
