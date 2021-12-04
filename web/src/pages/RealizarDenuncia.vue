<template>
  <div>
    <div>
      <PageTitle
        title="Realizar una denuncia"
        subtitle="En esta sección podrá realizar una denuncia"
      />
    </div>

    <div>
      <ComplaintForm />
    </div>
  </div>
</template>

<script>
import PageTitle from "../components/PageTitle.vue";
import ComplaintForm from "../components/ComplaintForm.vue";

export default {
  name: "RealizarDenuncia",
  title: "Realizar una Denuncia",
  components: {
    PageTitle,
    ComplaintForm,
  },
};
</script>


<style>
</style>