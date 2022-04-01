import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'
import titleMixin from './mixins/titleMixin'
import "leaflet/dist/leaflet.css"
import store from './store'
import './registerServiceWorker'

createApp(App).use(store).use(router).mixin(titleMixin).mount('#app')