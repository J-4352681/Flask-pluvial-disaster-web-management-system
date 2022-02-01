const axios = require('axios')

const axios_instace = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL
});

export const complaintsChartData =
  async function() {
    try {
      console.log('PITO1')
      console.log(process.env.VUE_APP_BASE_URL)
      let response = await axios_instace.get('/estadisticas/by-category')
      return response.data.stats
    }
    catch(error) {
      console.log(error)
      return {}
    }
  }

export const userChartData =
  async function() {
    try {
      console.log('PITO2')
      let response = await axios_instace.get('/estadisticas/by-user')
      return response.data.stats
    }
    catch(error) {
      console.log(error)
      return {}
    }
  }