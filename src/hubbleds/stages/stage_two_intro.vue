<template>
  <v-container
    class="py-0"
  >
    <v-row
      justify="center"
    >
      <v-col cols="12">
        <py-two-intro-slideshow />
      </v-col>
    </v-row>
  </v-container>
</template>

<style>

.theme--dark .MathJax {
  color: white !important;
}

.theme--light .MathJax {
  color: black !important;
}

.JaxEquation .MathJax {
  margin: 16px auto !important;
}

.v-container .v-card__text {
  font-size: 18px !important;
  line-height: 1.5 !important;
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
