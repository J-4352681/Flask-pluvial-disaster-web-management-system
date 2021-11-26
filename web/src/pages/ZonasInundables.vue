<template>
    <div>
        <h3>Zonas Inundables</h3>
        <list :headers="shownHeaders" :items="removeFields(zonas, shownHeaders)"/>
    </div>
</template>

<script>
import list from '../components/List.vue'

export default {
  name: 'ZonasInundables',
  title: 'Zonas Inundables',
  props: {

  },
  components: {
    list
  },
  data() {
    return {
      zonas: [],
      shownHeaders: ['color', 'nombre'],
      removeFields: function(objArray, headersArray) {
        let newArray = [];
        let a;
        objArray.forEach(function(obj) {
          a = {};
          headersArray.forEach(header => a[header] = obj[header]);
          newArray.push(a);
        });
        return newArray
      }
    }
  },
  mounted() {
    fetch('http://127.0.0.1:5000/api/zonas_inundables/')
      .then(res => res.json())
      .then(data => this.zonas = data.zonas)
      .catch(err => console.log(err.message))
  }
}
</script>


<style>
.zona{

}
</style>