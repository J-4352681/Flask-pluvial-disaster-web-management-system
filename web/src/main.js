import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import titleMixin from './mixins/titleMixin'
import "leaflet/dist/leaflet.css"

createApp(App).use(router).mixin(titleMixin).mount('#app')