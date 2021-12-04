<template>
  <div class="denuncias-form">
    <div class="column-map">
      <div style="height: 350px">
        
        <MapLinesMarkers
          style="height: 80%; width: 100%"
          :zoom="zoom"
          :center="center"
          @update:zoom="zoomUpdated"
          @update:center="centerUpdated"
          @update:bounds="boundsUpdated"
        >
         
        </MapLinesMarkers>
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
            <template v-for="cat in categoryList">
              <option :value="cat.id">{{ cat.name }}</option>
            </template>
          </select>
        </div>

        <div class="form-input">
          <label for="title">Título</label>
          <input
            id="title"
            v-model="title"
            name="title"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="description">Descripción</label>
          <input
            id="description"
            v-model="description"
            name="description"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="coordinates">Coordenadas</label>
          <input
            id="coordinates"
            v-model="coordinates"
            name="coordinates"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="surname">Apellido</label>
          <input
            id="surname"
            v-model="surname"
            name="surname"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="name">Nombre</label>
          <input
            id="name"
            v-model="name"
            name="name"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="telephone">Teléfono</label>
          <input
            id="telephone"
            v-model="telephone"
            name="telephone"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-input">
          <label for="email">Correo de contacto</label>
          <input
            id="email"
            v-model="email"
            name="email"
            type="email"
            required
            :disabled="loading"
          />
        </div>

        <div class="form-button">
          <button type="submit" :disabled="loading">Enviar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import MapLinesMarkers from "../components/MapLinesMarkers.vue";
export default {
  name: "FormularioDenuncia",
  title: "Formulario de una Denuncia",
  components: {
    MapLinesMarkers,
  },
  data() {
    return {
      place: "",
      category: "",
      title: "",
      description: "",
      coordinates: "",
      surname: "",
      name: "",
      telephone: "",
      email: "",
      loading: false,
      categoryList: [],
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 3,
      center: [47.41322, -1.219482],
      bounds: null,
    };
  },
  created() {
    this.loading = true;
    fetch("http://localhost:5000/api/denuncias/categorias")
      .then((res) => res.json())
      .then((res) => (this.categoryList = res.categorias))
      .catch((reason) => console.error(reason))
      .finally(() => (this.loading = false));
  },
  methods: {
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
      console.log("submt form");
      this.loading = true;
      e.preventDefault();
      fetch(
        "https://admin-grupo38.proyecto2021.linti.unlp.edu.ar/api/denuncias",
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
        coordinates: this.coordinates,
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
</style>