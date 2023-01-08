<template>
  <v-container>
    <v-row v-if="show_team_interface">
      <v-col>
        <v-btn
          color="error"
          class="black--text"
          @click="() => {
            console.log('stage state:', stage_state);
            console.log('story state:', story_state);
            }"
        >
          State
        </v-btn>
        Marker: {{ stage_state.marker }}
      </v-col>
    </v-row>
    <v-row
      class="d-flex align-stretch"
    >
      <v-col
        cols="12"
        lg="4"
      >
        <guideline-angsize-meas1
          v-if="stage_state.marker == 'ang_siz1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas2
          v-if="stage_state.marker == 'ang_siz2'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas2b
          v-if="stage_state.marker == 'ang_siz2b'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas3
          v-if="stage_state.marker == 'ang_siz3'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas4
          v-if="stage_state.marker == 'ang_siz4'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas5a
          v-if="stage_state.marker == 'ang_siz5a'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas6
          v-if="stage_state.marker == 'ang_siz6'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-repeat-remaining-galaxies
          v-if="stage_state.marker == 'rep_rem1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-estimate-distance1
          v-if="stage_state.marker == 'est_dis1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-estimate-distance2
          v-if="stage_state.marker == 'est_dis2'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
      </v-col>
      <v-col
        cols="12"
        lg="8"
      >
        <v-row>
          <v-col
            class="py-0"
          >
            <v-card
              :color="stage_state.csv_highlights.includes(stage_state.marker) ? 'info' : 'black'"
              :class="stage_state.csv_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
              outlined
            >
              <py-distance-tool />
            </v-card>
          </v-col>
        </v-row>
        <v-row
          v-if="stage_state.indices[stage_state.marker] > stage_state.indices['ang_siz5']"
        >
          <v-col
            cols="6"
            offset="3"
          >
            <py-dosdonts-slideshow />
          </v-col>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        lg="8"
        offset-lg="4"
        v-if="stage_state.distance_sidebar"
      >
        <py-distance-sidebar />
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        lg="4"
      >
        <guideline-choose-row1
          v-if="stage_state.marker == 'cho_row1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-angsize-meas5
          v-if="stage_state.marker == 'ang_siz5'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-choose-row2
          v-if="stage_state.marker == 'cho_row2'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />    
        <guideline-estimate-distance3
          v-if="stage_state.marker == 'est_dis3'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-estimate-distance4
          v-if="stage_state.marker == 'est_dis4'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-fill-remaining-galaxies
          v-if="stage_state.marker == 'fil_rem1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-stage-two-complete
          v-if="stage_state.marker == 'two_com1'" 
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
      </v-col>
      <v-col
        cols="12"
        lg="8"
      >
        <v-card
          :color="stage_state.table_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.table_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <jupyter-widget :widget="widgets.distance_table" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<style>

.v-dialog .v-card__text {
  font-size: 18px !important;
}

.v-radio label.theme--dark{
  color: white !important;
}
.v-radio label.theme--light{
  color: black !important;
}

.v-alert .v-input--radio-group+.v-alert, .v-dialog .v-input--radio-group+.v-alert {
  background-color: #000b !important;
}

</style>


<script>

module.exports = {
  methods: {
    scrollIntoView: function(entries, observer, isIntersecting) {
      if (isIntersecting) {
        entries[0].target.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    }
  }
}

</script>
