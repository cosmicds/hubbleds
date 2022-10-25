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
      Trend Lines
    </h3>
    <div
      class="mb-4"
    >
    <p>
        Even when data are messy, it is possible to explore relationships between the quantities being graphed. Scientists do this by fitting a <strong>model</strong> to the data. 
      </p>
      <p>
        Since we saw a trend in the larger class data set, let's start with a trend line. A <strong>trend line</strong> follows the observed trend in the graphed data.
      </p>
      <p>
        Click <v-icon>mdi-message-draw</v-icon> in the Toolbar to activate the drawing tool and try drawing a trend line through your data points.
      </p>
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
            state.marker = 'tre_lin1'
          "
        >
          back
        </v-btn>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.trend_line_drawn"
      >
        <div
          style="font-size: 16px;"
        >
          Draw a trend line.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.trend_line_drawn"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'bes_fit1'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>







