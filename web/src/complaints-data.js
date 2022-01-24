const axios = require('axios')

export const complaintsChartData =
  async function() {
    try {
      let response = await axios.get('http://127.0.0.1:5000/api/estadisticas/by-category')
      return response.data.stats
    }
    catch(error) {
      console.log(error)
      return {}
    }
  }
export default complaintsChartData;