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
      Best Fit Line
    </h3>
    <div class="mb-4">
      <p>
        Depending on how messy your dataset is, it may be tricky to draw a trendline. We can use a formula to calculate the <strong>best-fit line</strong>, no matter how messy your data are. A best-fit-line minimizes the total distance between all the data points and the line. Let’s see how the calculated best-fit line compares with your trend line.
      </p>
      <p>
        Click on <v-icon>mdi-chart-timeline-variant</v-icon> in the Toolbar to display the best fit line.
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
      <v-col>
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'tre_lin2';
          "
        >
          back
        </v-btn>
      </v-col>
      <v-spacer></v-spacer>
      <v-col
        cols="6"
        class="shrink"
        v-if="!state.best_fit_clicked"
      >
        <div
          style="font-size: 16px;"
        >
          Click <v-icon>mdi-chart-timeline-variant</v-icon> to show best fit.
        </div>
      </v-col>
      <v-col
        class="shrink"
        v-if="state.best_fit_clicked"
      >
        <v-btn
          class="black--text"
          color="accent"
          elevation="2"
          @click="
            state.marker = 'age_uni1';
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>