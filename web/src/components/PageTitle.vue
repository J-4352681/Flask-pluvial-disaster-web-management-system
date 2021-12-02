<template>
  <section class="container">
    <div class="page-header">
      <h2 class="page-title">{{ title }}</h2>
      <h4 class="page-subtitle">{{ subtitle }}</h4>
    </div>
  </section>
</template>

<script>
export default {
  name: 'pageTitle',
  props: {
    title: String,
    subtitle: String
  }
}
</script>

<style>
  .page-header {
    text-align: left;
    border-bottom: 1px solid #e3e3e3;
  }

  @media (max-width: 768px) {
    .page-header {
      padding: 6% 0;
      margin: 3% 1%;
    }

    .page-subtitle {
      margin: 2%;
    }

    .page-title {
      margin: 3% 2%;
    }
  }

  @media (min-width: 768px) {
    .page-header {
      padding: 2% 0;
      margin: 10px 1%;
    }

    .page-subtitle {
      margin: 20px 2% 10px 2%;
    }

    .page-title {
      margin: 10px 2%;
    }
  }
</style>