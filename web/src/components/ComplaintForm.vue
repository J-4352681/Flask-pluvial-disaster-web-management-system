<template>
  <div class="denuncias-form">
    <div class="column-map">
      <div style="height: 350px">
        
        <l-map style="height: 600px" :zoom="zoom" :center="center">
          <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
          <l-marker :lat-lng="marker" :draggable="true" @drag="markerDrag">
          </l-marker>
        </l-map>
      </div>
    </div>
    <div class="column-form">
      <form id="app" @submit="submitForm">

        <div class="form-input">
          <label for="categoria_id">Categoría</label>
          <select v-model="categoria_id" required :disabled="loading">
            <option disabled value="">Elija una categoría</option>
            <template v-for="cat in categoryList" :key="cat.id">
              <option :value="cat.id">{{ cat.name }}</option>
            </template>
          </select>
        </div>

        <div class="form-input">
          <label for="titulo">Título</label>
          <input id="titulo" v-model="titulo" name="titulo" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="descripcion">Descripción</label>
          <input id="descripcion" v-model="descripcion" name="descripcion" required :disabled="loading" />
        </div>

        <div class="form-input d-none">
          <label for="coordenadas">Coordenadas</label>
          <input id="coordenadas" v-model="coordenadas" name="coordenadas" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="apellido_denunciante">Apellido</label>
          <input id="apellido_denunciante" v-model="apellido_denunciante" name="apellido_denunciante" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="nombre_denunciante">Nombre</label>
          <input id="nombre_denunciante" v-model="nombre_denunciante" name="nombre_denunciante" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="telcel_denunciante">Teléfono</label>
          <input id="telcel_denunciante" v-model="telcel_denunciante" name="telcel_denunciante" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="email_denunciante">Correo de contacto</label>
          <input id="email_denunciante" v-model="email_denunciante" name="email_denunciante" type="email_denunciante" required :disabled="loading" />
        </div>

        <div class="form-button">
          <button type="submit" :disabled="loading">Enviar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker} from '@vue-leaflet/vue-leaflet';

export default {
  name: "FormularioDenuncia",
  titulo: "Formulario de una Denuncia",
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data() {
    let marker_init_value = [{lat:-34.92149, lng: -57.954597}];
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 15,
      center: [-34.92149, -57.954597],
      bounds: null,
      marker: marker_init_value[0],
      
      categoria_id: "",
      titulo: "",
      descripcion: "",
      coordenadas: JSON.stringify(marker_init_value),
      apellido_denunciante: "",
      nombre_denunciante: "",
      telcel_denunciante: "",
      email_denunciante: "",
      loading: true,
      categoryList: [],
    };
  },
  created() {
    fetch(process.env.VUE_APP_COMPLAINT_CATEGORY_URL)
      .then((res) => res.json())
      .then((res) => this.categoryList = res.categorias)
      .catch((reason) => console.error(reason))
      .finally(() => this.loading = false);
  },
  methods: {
    markerDrag(e) {
      this.coordenadas = '[' + JSON.stringify(e.latlng) + ']';
    },
    zoomUpdated(zoom) {
      this.zoom = zoom;
    },
    centerUpdated(center) {
      this.center = center;
    },
    boundsUpdated(bounds) {
      this.bounds = bounds;
    },
    submitForm(e) {
      this.loading = true;
      e.preventDefault();
      fetch(
        process.env.VUE_APP_COMPLAINT_POST_URL,
        {
          // Adding method type
          method: "POST",

          // Adding body or contents to send
          body: JSON.stringify(this.getFormData()),

          // Adding headers to the request
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
          },
        }
      )
        .then((res) => res.json())
        .then((res) => console.log(res))
        .catch((reason) => console.error(reason))
        .finally(() => (this.loading = false));
    },
    getFormData() {
      return {
        categoria_id: this.categoria_id,
        titulo: this.titulo,
        descripcion: this.descripcion,
        coordenadas: JSON.parse(this.coordenadas),
        apellido_denunciante: this.apellido_denunciante,
        nombre_denunciante: this.nombre_denunciante,
        telcel_denunciante: this.telcel_denunciante,
        email_denunciante: this.email_denunciante,
      };
    },
  },
};
</script>


<style>
.denuncias-form {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-left: 15px;
}

.denuncias-form .column-map,
.denuncias-form .column-form {
  padding: 40px;
  width: 50%;
}

.denuncias-form .form-input {
  display: flex;
  width: 350px;
  justify-content: space-between;
  margin-bottom: 10px;
}

.denuncias-form label {
  display: block;
  width: 140px;
  text-align: left;
}

.denuncias-form .form-button {
  margin-top: 15px;
}

.d-none {display: none !important}
</style>