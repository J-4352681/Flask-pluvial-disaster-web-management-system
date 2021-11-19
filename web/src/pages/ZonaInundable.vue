<template>
    <p>Zona Inundable de id {{$route.params.id}}</p>
</template>

<script>
export default {
  name: 'ZonaInundable',
  title () {
    return `Zonas Inundables > ${this.$route.params.id}`
  },
  props: {

  },
  components: {
      
  }
}
</script>


<style>

</style>