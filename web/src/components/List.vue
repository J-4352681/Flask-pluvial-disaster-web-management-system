<template>
  <table class="table">
    <thead>
      <tr class="table-header">
        <th v-for="header in headers" :key="header" class="header-field">{{ header }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in removeFields(items, headers)" :key="item.id" class="table-item">
        <td v-for="value in item" :key="value" @click="onClick(item)" class="table-item-field">{{ value }}</td>
      </tr>
    </tbody>
  </table>

</template>

<script>
  export default {
    name: 'List',
    props: {
      items: Array,
      headers: Array
    },
    components: {
      
    },
    data() {
      return {
        removeFields: function(objArray, headersArray) {
            let newArray = [];
            let a;
            objArray.forEach(function(obj) {
              a = {};
              headersArray.forEach(function(header) {
                if(Object.keys(obj).includes(header)) a[header] = obj[header];
                else a[header] = "";
              });
              newArray.push(a);
            });
          return newArray
        }
      }
    },
    methods: {
      onClick(e) {
        console.log(e)
        if ( e.id ){
          var url = '/zonas-inundables/' + e.id
          this.$router.push(url);
        }
      }
    }
  }
</script>

<style>
  .table {
    margin: 2vw 3vw;
    display: flex;
    flex-direction: column;
  }

  .table-header {
    padding: 0 1vw;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    border-bottom: 1px solid gray
  }

  .header-field {
    padding: .5vw;
    display: flex;
    width: 100%;
  }

  .table-item-field {
    padding: .5vw;
    display: flex;
    width: 100%;
  }

  .table-item {
    padding: .75vw;
    margin: .25vw;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    border-radius: 5px;
    color: gray;
  }
  .table-item:hover {
    background: #e3e3e3;
    cursor: pointer;
  }
</style>