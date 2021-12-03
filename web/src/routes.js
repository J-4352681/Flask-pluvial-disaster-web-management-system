import { createRouter, createWebHistory } from 'vue-router'

import Home from './pages/Home.vue'
import MapaEmergencias from './pages/MapaEmergencias.vue'
import ZonasInundables from './pages/ZonasInundables.vue'
import ZonaInundable from './pages/ZonaInundable.vue'
import RealizarDenuncia from './pages/RealizarDenuncia.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/mapa-emergencias',
        name: 'MapaEmergencias',
        component: MapaEmergencias
    },
    {
        path: '/zonas-inundables',
        name: 'ZonasInundables',
        component: ZonasInundables
    },
    {
        path: '/zonas-inundables/:id',
        name: 'ZonaInundable',
        component: ZonaInundable
    },
    {
        path: '/denuncias',
        name: 'RealizarDenuncia',
        component: RealizarDenuncia
    },
]

const router = createRouter({
    mode: 'history',
    history: createWebHistory(),
    routes
})

export default router