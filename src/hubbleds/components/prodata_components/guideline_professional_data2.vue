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
    <p>Is your age estimate higher than or lower than Hubble's age estimate? </p>
      <v-container
        class="px-0"
        fluid
      >
        <mc-radiogroup
          :radio-options="[
            'Our class got a higher age estimate than Hubble',
            'Our class got a lower age estimate than Hubble.'
          ]"
          :feedbacks="[
            'Correct! Because the slope of the trend in our data is shallower than the trend in Hubble\'s data, our age estimate must be higher ',
            'Remember, the slope of the trend in our data is shallower than the trend in Hubble\'s data, so our age estimate must be higher.'
          ]"
          :correct-answers="[0]"
          :neutral-answers='[1]'
          :selected-callback="(state) => { $emit('ready'); }"
          score-tag="pro-dat2"
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
                state.marker = 'pro_dat1';
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
                state.marker = 'pro_dat3';
              }
            "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>





