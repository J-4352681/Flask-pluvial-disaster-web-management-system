import { createRouter, createWebHistory } from 'vue-router'

import Home from './pages/Home.vue'
import MapaEmergencias from './pages/MapaEmergencias.vue'
import ZonasInundables from './pages/ZonasInundables.vue'
import ZonaInundable from './pages/ZonaInundable.vue'
import RealizarDenuncia from './pages/RealizarDenuncia.vue'
import MapaDenuncias from './pages/MapaDenuncias.vue'
import Estadisticas from './pages/Estadisticas.vue'

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
    {
        path: '/mapa-denuncias',
        name: 'MapaDenuncias',
        component: MapaDenuncias
    },
    {
        path: '/estadisticas',
        name: 'Estadisticas',
        component: Estadisticas
    },
]

const router = createRouter({
    mode: 'history',
    history: createWebHistory(),
    routes
})

export default router