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
      console.log('primeros');
      console.log(response);
      return response.json();
    }).then((json) => {
      console.log(json);
      this.fetched_complaints = json.denuncias;
      console.log(this.fetched_complaints);
    }).catch((e) => {
      console.log('problema');
      console.log(e)
    });
  }
}
</script>


<style>

</style>