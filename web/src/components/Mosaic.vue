<template>
  <section class="container">
    <div class="mosaic-header">
      <h2 class="mosaic-title">{{ title }}</h2>
    </div>
    <div class="mosaic-table">
      <router-link class="mosaic-element" v-for='element in elements' :key='element.title' :to='element.linkName'>
        <h4 class="mosaic-element-title">{{ element.title }}</h4>
        <p class="mosaic-element-description">{{ element.description }}</p>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: 'mosaic',
  props: {
    title: String,
    elements: Array
  },
  components: {

  }
}
</script>

<style>
  .mosaic-title {
    font-size: 15pt;
  }

  .mosaic-element {
    text-decoration: none;
    display: block;

    text-align: justify;
    border-radius: 5px;
    box-shadow: 0 0 10px #e3e3e3;
  }
  .mosaic-element:hover {
    background: #e3e3e3;
    cursor: pointer;
  }

  .mosaic-header {
    text-align: left
  }

  .mosaic-table {
    margin: 2%;
  }

  .mosaic-element-description {
    color: gray;
  }

  .mosaic-element-title {
    margin: 1% 0;
    color: #595959;
  }

  @media (max-width: 768px) {
    .mosaic-element {
      padding: 5%;
      margin: 3% 0 2% 0;
    }

    .mosaic-title {
      margin: 5% 2%;
    }
  }

  @media (min-width: 768px) {
    .mosaic-table {
      display: flex;
      flex-flow: row wrap;
      justify-content: center;
    }

    .mosaic-element {
      padding: 2%;
      width: 40%;
      margin: 10px;
    }

    .mosaic-title {
      margin: 15px 2%;
    }
  }
</style>