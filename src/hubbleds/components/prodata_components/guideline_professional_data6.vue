<!-- # multiple choice -->
<template>
  <v-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
  >
    <h3
      class="mb-4"
    >
      Professional Data
    </h3>
    <div
      class="mb-4"
    >
      Is your age estimate higher or lower than the HST team's estimate? 
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class got a higher age estimate than HST',
            'Our class got a lower age estimate than HST',
          ]"
          :feedbacks="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ?
  ['Correct! The slope of best fit for our data is shallower than it is for the HST data', 'Try again! Compare the slope of best fit for our data to the slope for the HST data'] :
  ['Try again! Compare the slope of best fit for our data to the slope for the HST data','Correct! The slope of best fit for our data is steeper than it is for the HST data', ]"
          :correct-answers="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ? [0] : [1]"
          :neutral-answers="(parseFloat(state.hst_age) < parseFloat(Math.round(state.our_age).toFixed(0))) ? [1] : [0]"
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat6"
        >
        </mc-radiogroup>
      </v-container>
    </div>
    
    <v-divider
      class="my-4"
    >
    </v-divider>

    <v-row
      align="center"
      no-gutters
    >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.marker = 'pro_dat5';
              }
            "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.prodata_response"
      >
        <div
          style="font-size: 16px;"
        >
          Choose a response.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.prodata_response"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
              () => {
                state.prodata_response = false;
                state.marker = 'pro_dat7';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>
