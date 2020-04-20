<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <NameGenerator msg="Generate Some Random names"/>
  </div>
</template>

<script>
// @ is an alias to /src
import NameGenerator from '@/components/NameGenerator.vue'

export default {
  name: 'Home',
  components: {
    NameGenerator
  }
}
</script>
