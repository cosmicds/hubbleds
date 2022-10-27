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
        Now that you've drawn what conclusions you can from looking at individual students' measurements, let's turn back to your whole class's dataset.
      </p>
      <p>
        Click <v-icon>mdi-message-draw</v-icon> in the Toolbar to activate the drawing tool and try drawing a trend line through your class's data points.
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
            state.marker = 'con_int2'
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
            state.marker = 'bes_fit1c'
          "
        >
          next
        </v-btn>
      </v-col>
    </v-row>
  </v-alert>
</template>