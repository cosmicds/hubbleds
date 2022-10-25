<template>
  <v-btn
    class="my-2"
    block
    color="secondary"
    elevation="2"
    @click.stop="() => { dialog = true; state.dos_donts_opened = true }"
  >
    measurement dos and donts

    <v-dialog
        v-model="dialog"
        persistent
        max-width="1000px"
    >
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
          >
            {{ currentTitle }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <span
            @click="
              () => {
                $emit('close');
                dialog = false;
                if (step == 8) {
                  step = 0;
                }
              }
            "
          >
            <v-btn icon>
              <v-icon> mdi-close </v-icon>
            </v-btn>
          </span>
        </v-toolbar>

          <v-window
            v-model="step"
            style="height: 70vh;"
            class="overflow-auto"
          >

          <v-window-item :value="0" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4"> Angular Size Measuring Tips </h3>
                    <p>
                      Measuring the galaxy angular sizes can be tricky. In this slideshow, we will walk you through DOs and DON’Ts for some different situations you may encounter. 
                    </p>
                    <p>
                      If you are having difficulty identifying the edges of fainter galaxies, it may help to adjust the contrast on your monitor.
                    </p>
                    <p>
                      These are just guidelines. Use your judgment and do the best you can.
                    </p>
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
                    <h3 class="mb-4">Wait for Galaxies to Fully Load</h3>
                    <p>
                      Depending on your internet connection, it might take a few moments for a galaxy to load at its full resolution. (Once in a while, the image gets stuck at a partial load. If this happens, click the flag button in the tool bar to remove the galaxy. You will have to return to Stage 1 to select another galaxy and re-measure its spectral line and velocity.)
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/IL-Do.png`"
                    ></v-img>
                    <h4> DO: </h4> 
                    <p>
                      Wait for the image to fully load before measuring the angular size
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/IL-Dont.png`"
                    ></v-img>
                    <h4>DON'T : </h4> 
                    <p>
                      Try to measure the angular size while the image load is still in progress
                    </p>
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
                    <h3 class="mb-4"> Elongated Galaxies </h3>
                    <p>
                      Many galaxies appear elongated. 
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/LS-Do.png`"
                    ></v-img>
                    <h4>DO:</h4> 
                    <p>
                      Measure across the longest part of the galaxy 
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/LS-Dont.png`"
                    ></v-img>
                    <h4>DON’T: </h4> 
                    <p>
                      Measure across a short dimension
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>

<!-- 
          <v-window-item :value="3" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4"> Hazy Elliptical Galaxies </h3>
                    <p>
                      Many elliptical galaxies have a very faint hazy border. That haze is usually part of the galaxy and should be included in your measurement. (If you can’t see the haze in these images, you may need to adjust the contrast on your monitor. Do the best you can.)
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                    class="d-flex flex-column"
                    height="100%"
                    flat
                    tile
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/EH-Do.png`"
                    ></v-img>
                    <h4>DO: </h4> 
                    <p>
                      Include as much fuzzy haze as you can see
                    </p>  
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/EH-Dont.png`"
                    ></v-img>
                    <h4>DON’T: </h4> 
                    <p>
                      Ignore the fuzzy haze around the galaxy edge
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>
 -->

<!--  
          <v-window-item :value="4" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4"> Faint Irregular Galaxies </h3>
                    <p>
                     Some galaxies (especially irregulars) are small and faint and appear as a wispy smudge on the screen. Again, adjust the contrast on your monitor as well as you can and do your best.
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                    class="d-flex flex-column"
                    height="100%"
                    flat
                    tile
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/IF-Maybe2.png`"
                    ></v-img>
                    <h4>OK: </h4> 
                    <p>
                      Maybe there is a faint haze around the brighter center. If you see it, you can include it.
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/IF-Maybe1.png`"
                    ></v-img>
                    <h4>OK: </h4>  
                    <p>
                      Do your best to pick out the galaxy edge.
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>
 -->
          
          <v-window-item :value="3" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4"> Measure the Entire Galaxy </h3>
                    <p>
                     Sometimes it is tempting to focus on only the brightest part of the galaxy and ignore fainter parts beyond the center. Be sure to measure the entire galaxy.
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/BS-Do.png`"
                    ></v-img>
                    <h4>DO: </h4>  
                    <p>
                     Measure across the entire galaxy
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/BS-Dont.png`"
                    ></v-img>
                    <h4>DON'T: </h4> 
                    <p>
                      Ignore the fainter region beyond the bright center
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>

<!-- 
          <v-window-item :value="4" 
            class="no-transition"
          >
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4">Field with Multiple Objects</h3>
                    <p>
                      Some fields have multiple objects, including foreground stars or other galaxies.
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="4"
                    class="d-flex flex-column"
                    height="100%"
                    flat
                    tile
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Multi-Do.png`"
                    ></v-img>
                    <h4>DO: </h4> 
                    <p>
                      Measure the SINGLE object in the center of the field of view
                    </p>
                  </v-col>
                  <v-col cols="4">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Multi-DONT1.png`"
                    ></v-img>
                    <h4>DON'T: </h4> 
                    <p>
                      Measure across multiple objects
                    </p>
                  </v-col>
                  <v-col cols="4">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Multi-DONT2.png`"
                    ></v-img>
                    <h4>DON'T: </h4> 
                    <p>
                      Measure an object that is not in the center of the field of view. 
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>
 -->

          <v-window-item :value="4" class="no-transition">
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4"> Zoomed In Galaxies </h3>
                    <p>
                      Some nearby galaxies are larger than the default field of view. Be sure to zoom out far enough to see the entire galaxy. (Roll the mouse wheel forward/backward or press z-x).
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/TC-Do.png`"
                    ></v-img>
                    <h4>DO: </h4>  
                    <p>
                      Zoom out far enough to see your entire galaxy before measuring
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/TC-Dont.png`"
                    ></v-img>
                    <h4>DON’T: </h4> 
                    <p>
                      Try to measure the angular size while too zoomed in
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
                  <v-col>
                    <h3 class="mb-4"> Field with Multiple Objects </h3>
                    <p>
                      Some fields have multiple objects in them such as stars or other galaxies. Sometimes a galaxy even has a merging companion (as shown below) or appears in a cluster of galaxies. Do your best and include only the galaxy that is centered in the field of view.
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="6"
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Col-Do.png`"
                    ></v-img>
                    <h4>DO: </h4>  
                    <p>
                      Measure the galaxy in the center of the field
                    </p>
                  </v-col>
                  <v-col cols="6">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Col-Dont.png`"
                    ></v-img>
                    <h4>DON’T: </h4> 
                    <p>
                      Measure across both galaxies, and DON'T measure other galaxies that are not in the center of the field
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>

<!-- 
          <v-window-item :value="6" 
            class="no-transition"
          >
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col>
                    <h3 class="mb-4">Galaxy Cluster</h3>
                    <p>
                      A galaxy cluster is a group of galaxies bound together by gravity. Be aware that each galaxy in the cluster is a distinct object. Don’t mistakenly measure across the entire group of galaxies.
                    </p>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col
                    cols="4"
                    class="d-flex flex-column"
                    height="100%"
                    flat
                    tile
                  >
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Cluster-Do.png`"
                    ></v-img>
                    <h4>DO: </h4> 
                    <p>
                      Measure the SINGLE object in the center of the field of view
                    </p>
                  </v-col>
                  <v-col cols="4">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Cluster-DONT1.png`"
                    ></v-img>
                    <h4>DON'T: </h4> 
                    <p>
                      Measure across multiple objects
                    </p>
                  </v-col>
                  <v-col cols="4">
                    <v-img
                      class="mb-4 mx-a"
                      contain
                      :src="`${state.image_location_dosdonts}/Cluster-DONT2.png`"
                    ></v-img>
                    <h4>DON'T: </h4> 
                    <p>
                      Measure an object that is not in the center of the field of view.
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item> 
 -->

          <v-window-item :value="6" class="no-transition">
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <h3 class="mb-4"> That’s it! </h3>
                      <p>
                        Did you find a weird case we didn’t cover? Do your best, or try consulting with a neighbor or your instructor.
                      </p>
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
            @click="step--"
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
                :disabled="n > max_step_completed + 7"
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
            :disabled="step > max_step_completed + 7"
            v-if="step < length-1"
            class="black--text"
            color="accent"
            depressed
            @click="step++;"
          >
            next
          </v-btn>
          <v-btn
            v-if = "step == length-1"
            color="accent"
            class="black--text"
            depressed
            @click="
              () => {
                $emit('close');
                dialog = false;
                step = 0;
              }
            "
          >
            done
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-btn>
</template>

<style>
.no-transition {
  transition: none;
}
</style>
