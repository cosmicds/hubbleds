<template>
  <scaffold-alert
    color="info"
    class="mb-4 mx-auto"
    max-width="800"
    elevation="6"
    title-text="Introducing the Guidelines"
    @next="state.marker = 'sel_gal1'"
    :allow-back="false"
  >
    <template #back-content>
      <div>
        Use left menu to return to Introduction.<br>
        (Open/close menu with <v-icon class="white--text">mdi-menu</v-icon> button in upper left)
      </div>
    </template>
    <div
      class="mb-4"
    >
      <p>
        <strong>These orange boxes will GUIDE you as you move through the story.</strong>
      </p>
      <p>
        The information in the guideline boxes will suggest what you should focus on, or what you should do next.
      </p>
      <p>
        The images, tables, or graph where the guideline suggests action will also be highlighted with an <strong>orange outline</strong>.
      </p>
    </div>
    
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
