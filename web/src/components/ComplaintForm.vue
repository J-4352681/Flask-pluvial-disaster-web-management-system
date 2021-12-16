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
          <label for="place">Lugar</label>
          <input
            id="place"
            v-model="place"
            type="text"
            place="place"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="category">Categoría</label>
          <select v-model="category" required :disabled="loading">
            <option disabled value="">Elija una categoría</option>
            <template v-for="cat in categoryList" :key="cat.id">
              <option :value="cat.id">{{ cat.name }}</option>
            </template>
          </select>
        </div>

        <div class="form-input">
          <label for="title">Título</label>
          <input id="title" v-model="title" name="title" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="description">Descripción</label>
          <input id="description" v-model="description" name="description" required :disabled="loading" />
        </div>

        <div class="form-input d-none">
          <label for="coordinates">Coordenadas</label>
          <input id="coordinates" v-model="coordinates" name="coordinates" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="surname">Apellido</label>
          <input id="surname" v-model="surname" name="surname" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="name">Nombre</label>
          <input id="name" v-model="name" name="name" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="telephone">Teléfono</label>
          <input id="telephone" v-model="telephone" name="telephone" required :disabled="loading" />
        </div>

        <div class="form-input">
          <label for="email">Correo de contacto</label>
          <input id="email" v-model="email" name="email" type="email" required :disabled="loading" />
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
  title: "Formulario de una Denuncia",
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

      place: "",
      category: "",
      title: "",
      description: "",
      coordinates: JSON.stringify(marker_init_value),
      surname: "",
      name: "",
      telephone: "",
      email: "",
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
      this.coordinates = '[' + JSON.stringify(e.latlng) + ']';
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
            "Content-type": "application/json; charset=UTF-8",
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
        place: this.place,
        category: this.category,
        title: this.title,
        description: this.description,
        coordinates: this.coordinates.replaceAll("'", '"'),
        surname: this.surname,
        name: this.name,
        telephone: this.telephone,
        email: this.email,
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