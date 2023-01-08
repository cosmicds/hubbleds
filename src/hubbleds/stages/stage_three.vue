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

    <!--------------------- TABLE ROW ----------------------->
    <v-row
      class="d-flex align-stretch"
    >
      <v-col
        cols="12"
        lg="4"
      >
        <guideline-explore-data
          v-if="stage_state.marker == 'exp_dat1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-age-universe-estimate3
          v-if="stage_state.marker == 'age_uni3'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-age-universe-estimate4
          v-if="stage_state.marker == 'age_uni4'"
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
          <v-lazy>
            <jupyter-widget :widget="widgets.fit_table"/>
          </v-lazy>
        </v-card>
      </v-col>
    </v-row>

    <!--------------------- OUR DATA HUBBLE VIEWER ----------------------->

    <v-row
      class="d-flex align-stretch"
      v-if="stage_state.indices[stage_state.marker] > stage_state.indices['exp_dat1'] && stage_state.indices[stage_state.marker] <= stage_state.indices['sho_est2']"
    >
      <v-col
        cols="12"
        lg="4"
      >
        <guideline-trends-data-mc1
          v-if="stage_state.marker == 'tre_dat1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.trend_response = true" />
        <guideline-trends-data2
          v-if="stage_state.marker == 'tre_dat2'"
          :state="stage_state"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.trend_response = true" />
        <guideline-trends-data-mc3
          v-if="stage_state.marker == 'tre_dat3'"
          :state="stage_state"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.trend_response = true" />
        <guideline-relationship-vel-dist-mc
          v-if="stage_state.marker == 'rel_vel1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.relvel_response = true" />
        <guideline-trend-lines1
          v-if="stage_state.marker == 'tre_lin1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-trend-lines-draw2
          v-if="stage_state.marker == 'tre_lin2'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-best-fit-line
          v-if="stage_state.marker == 'bes_fit1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-hubbles-expanding-universe1
          v-if="stage_state.marker == 'hub_exp1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-hubbles-expanding-universe2
          v-if="stage_state.marker == 'hub_exp2'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />          
        <guideline-running-race-mc
          v-if="stage_state.marker == 'run_rac1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView"
          @ready="stage_state.race_response = true" />
        <guideline-runners-vel-dist
          v-if="stage_state.marker == 'run_vel1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-age-universe
          v-if="stage_state.marker == 'age_uni1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-hypothetical-galaxy
          v-if="stage_state.marker == 'hyp_gal1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-age-race-equation
          v-if="stage_state.marker == 'age_rac1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-age-universe-equation2
          v-if="stage_state.marker == 'age_uni2'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-your-age-estimate
          v-if="stage_state.marker == 'you_age1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-shortcomings-est-reflect1
          v-if="stage_state.marker == 'sho_est1'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
        <guideline-shortcomings-est2
          v-if="stage_state.marker == 'sho_est2'"
          :state="stage_state"
          v-intersect.once="scrollIntoView" />
      </v-col>
      <v-col
        cols="12"
        lg="8"
      >
        <v-card
          :color="stage_state.my_galaxies_plot_highlights.includes(stage_state.marker) ? 'info' : 'black'"
          :class="stage_state.my_galaxies_plot_highlights.includes(stage_state.marker) ? 'pa-1 my-n1' : 'pa-0'"
          outlined
        >
          <v-row>
            <v-col cols="3">
              <py-layer-toggle/>
            </v-col>
            <v-col>
              <v-lazy>
                <jupyter-widget :widget="viewers.layer_viewer"/>
              </v-lazy>
            </v-col>
          </v-row>
        </v-card>
        <v-row>
          <v-col
            cols="10"
            offset="1"
          >
            <py-hubble-slideshow 
              :state="stage_state"
              v-if="stage_state.indices[stage_state.marker] > stage_state.indices['rel_vel1']" />  
          </v-col>
        </v-row>
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

.v-slider__thumb:hover, .v-slider__thumb-label-container:hover {
  cursor: grab;
}

.v-slider__thumb:active, .v-slider__thumb-label-container:active {
  cursor: grabbing;
}

</style>


<script>

module.exports = {
  mounted() {
    const config = { childList: true, subtree: true };
    const onMutation = (mutationList, observer) => {
      for (const mutation of mutationList) {
        if (mutation.type === 'childList') {
          const target = mutation.target;
          const viewerName = this.viewerName(target);
          if (viewerName !== null) {
            const resizeObserver = new ResizeObserver((entries) => {
              for (const entry of entries) {
                const pixelSize = entry.devicePixelContentBoxSize[0];
                const width = pixelSize.inlineSize;
                const nticks = Math.floor(width / 125);
                this.set_viewer_nticks({ nticks: nticks, axis: 'x', viewer: viewerName });
              }
            });
            resizeObserver.observe(target, { box: 'device-pixel-content-box' });
          }
        }
      }
    }
    const observer = new MutationObserver(onMutation);
    observer.observe(this.$el, config);
  },
  methods: {
    scrollIntoView: function(entries, observer, isIntersecting) {
      if (isIntersecting) {
        entries[0].target.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        });
      }
    },
    viewerName: function(node) {
      for (const key of Object.keys(this.viewers)) {
        if (node.classList.contains(key)) {
          return key;
        }
      }
      return null;
    }
  }
}

</script>
