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
      <span>Use left menu to return to Introduction.<br>(Press <v-icon>mdi-menu</v-icon> in upper left if menu is not open)</span>
    </template>
    <div
      class="mb-4"
    >
      <p>
        <b> These orange boxes will GUIDE you as you move through the story. </b>
      </p>
      <p>
        The information in the guideline boxes will suggest what you should focus on, or what you should do next.  
      </p>
      <p>
        The images, tables, or graph where the guideline suggests action will also be highlighted with an <b> orange outline.</b>
      </p>
    </div>
    
  </scaffold-alert>
</template>

<script>
module.exports = {
 props: ['state']
}
</script>
