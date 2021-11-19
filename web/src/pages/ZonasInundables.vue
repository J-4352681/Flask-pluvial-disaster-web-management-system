<template>
    <div>
        <p>Zonas Inundables</p>
        <router-link :to="{ name: 'ZonaInundable', params: { id: '4' }}" > Ir a la zona de id 4</router-link>
    </div>
</template>

<script>
export default {
  name: 'ZonasInundables',
  props: {

  },
  components: {
      
  }
}
</script>


<style>

</style>