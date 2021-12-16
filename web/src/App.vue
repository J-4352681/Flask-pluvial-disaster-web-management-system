<template>
    <div id="app">
        <NavBar/>
        <router-view/>
    </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
    name: 'App',
    components: {
        NavBar,
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
body {
    margin: 0;
}

@media (max-width: 360px) {
  .container {
    padding: 0 1%;
  }
}
@media (min-width: 360px) and (max-width: 768px) {
  .container {
    padding: 0 3%;
  }
}
@media (min-width: 768px) {
  .container {
    padding: 0 15%;
  }
}
</style>
