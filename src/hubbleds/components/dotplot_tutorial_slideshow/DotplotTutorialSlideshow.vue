<template>
  <!-- add persistant to prevent closing by clicking out -->
  <v-dialog
      v-model="dialog"
      max-width="1000px"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        block
        color="secondary"
        elevation="2"
        id="slideshow-button"
        @click.stop="() => { show_dialog(true); }"
      >
        Dot Plot Tutorial
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
          Dot Plot Tutorial
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <speech-synthesizer
          :root="() => this.$refs.content.$el"
          :autospeak-on-change="step"
          :speak-flag="dialog"
          :selectors="['div.v-toolbar__title', 'div.v-card__text.black--text', 'h3', 'p']"
          />
        <v-btn
          icon
          @click="() => { 
            show_dialog(false); 
            if (step === length-1) 
              { 
                tutorial_finished(); 
                set_step(0);  
              }
          }"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>

        <v-window
          v-model="step"
          class="overflow-auto"
        >
        <v-row>
          <v-col
            cols="12"
            lg="5"
            >
            
            <v-window-item :value="0" class="no-transition">
              <v-card-text>
                <v-container>
                  <p>
                    This is a <b>dot plot</b> for a set of velocity values similar to the measurements you are making. Each measured velocity value is represented by a single <b>dot</b>.
                  </p>
                  <p>
                    Dots are stacked within velocity <b>ranges</b> called <b>bins</b>.
                  </p>
                  <p>
                    The horizontal axis shows the measured velocity values.
                  </p>
                  <p>
                    The vertical axis shows how many measurements were made in a particular velocity bin.
                  </p>
                </v-container>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="1" class="no-transition">
              <v-card-text>
                <v-container>
                  <p>
                    As with the spectrum viewer, if you move your mouse left and right within the dot plot, the vertical marker will display the velocity value for the center of each bin.
                  </p>
                </v-container>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="2" class="no-transition">
              <v-card-text>
                <v-container>
                  <p>
                    Our data sample includes a very large range of velocity values, but most of the data points are clustered in one or more tall towers of dots between 9,000 to 13,000 km/s. 
                  </p>
                  <p>
                    Let's take a closer look at this cluster of measurements. 
                  </p>
                  <p>
                    Click <v-icon>mdi-select-search</v-icon> in the toolbar to activate the zoom tool.
                  </p>                    
                  <p>
                    Then click and drag across the cluster of velocity measurements to zoom in.
                  </p>
                </v-container>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="3" class="no-transition">
              <v-card-text>
                <v-container>
                  <p>
                    You should see that the tall towers of dots have split into smaller towers. If not, zoom in closer by clicking and dragging again, or click <v-icon>mdi-cached</v-icon> to reset the view and try again.
                  </p>
                  <p>
                    This happens because each tower of dots represents a <b>range</b> of velocity values. When you zoomed in, the data were rebinned across smaller velocity ranges.
                  </p>
                  <p>
                    That's all you need to know about dot plots for now. Click done to continue.  
                  </p>                      
                </v-container>
              </v-card-text>
            </v-window-item>  
          </v-col>
          <v-col
            cols="12"
            lg="7"
          >
           <jupyter-widget :widget="dotplot_viewer"/>
          </v-col>
        </v-row>
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
          @click="set_step(step-1)"
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
            <v-btn
              :input-value="active"
              icon
              @click="set_step(n-1);"
            >
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-spacer></v-spacer>
          <v-btn
          v-if="step < length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { set_step(step+1); }"
        >
          {{ step < length-1 ? 'next' : '' }}
        </v-btn>
        <v-btn
          v-if = "step == length-1"
          color="accent"
          class="black--text"
          depressed
          @click="() => { 
            show_dialog(false); 
            tutorial_finished();
            set_step(0); 
          }"
        >
          Done
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<style scoped>
.no-transition {
  transition: none;
}

.row {
  width: 100%;
  margin-left: 0 !important;
  margin-right: 0 !important;
}
</style>
