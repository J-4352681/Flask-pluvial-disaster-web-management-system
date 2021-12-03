<template>
    <div>
        <nav class="topnav" id="myTopnav">
            <router-link to='/'>Logo</router-link>
            <router-link to='/mapa-emergencias' active-class='active'>Mapa para Emergencias</router-link>
            <router-link to='/zonas-inundables' active-class='active'>Zonas Inundables</router-link>
            <router-link to='/denuncias' active-class='active'>Realizar una Denuncia</router-link>
            <router-link to='/estadisticas' active-class='active'>Estadisticas</router-link>
            <a href="javascript:void(0);" class="icon" v-on:click="toggleNavBar"> <!--Fix para responsive sacado de: https://www.w3schools.com/howto/howto_js_topnav_responsive.asp --> 
                <b>+</b>
            </a>
        </nav>
    </div>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
      toggleNavBar: function () {
        var x = document.getElementById("myTopnav")
        if (x.className === "topnav") {
            x.className += " responsive"
        } else {
            x.className = "topnav"
        }
      }
  }
}
</script>

<style>
.topnav {
  background-color: #333; /* Primary */
  overflow: hidden;
}

.topnav a {
  float: left;
  display: block;
  color: #f2f2f2; 
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #04AA6D; /* Accent */
  color: white;
}

.topnav .icon {
  display: none;
}

@media screen and (max-width: 600px) {
  .topnav a:not(:first-child) {display: none;}
  .topnav a.icon {
    float: right;
    display: block;
  }
}

@media screen and (max-width: 600px) {
  .topnav.responsive {position: relative;}
  .topnav.responsive a.icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a {
    float: none;
    display: block;
    text-align: left;
  }
}
</style>