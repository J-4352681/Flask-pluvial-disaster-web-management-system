<template>
    <p>Mapa de Denuncias</p>
</template>

<script>
export default {
  name: 'MapaDenuncias',
  title: 'Mapa de Denuncias',
  props: {

  },
  components: {
      
  },
  data () {
    return {
        fetched_complaints: []
    };
  },
  created() {
    //Denuncias
    fetch('https://127.0.0.1:5000/api/denuncias/all').then((response) => {
      return response.json();
    }).then((json) => {
      this.fetched_complaints = json.denuncias;
    }).catch((e) => {
      console.log(e)
    });
  }
}
</script>


<style>

</style>