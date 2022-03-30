const icons = {
	route: '/static/icons/',
	type: '.svg',
	names: [
		'add',
		'analytics',
		'eye',
		'pencil',
		'trash',
		'water',
		'waterIcon',
		'close',
		'person',
		'cloud-offline'
	]
};

const iconsAssets = icons.names
	.map((x) => icons.route + x + icons.type);

const maps = {
	route: '/static/map/',
	type: '.js',
	names: [
		'edit_route_map',
		'edit_zone_map',
		'geoman_init',
		'leaflet_init',
		'routingmachine_init',
		'show_route_map',
		'show_zone_map'
	]
};

const mapsAssets = maps.names
	.map((x) => maps.route + x + maps.type)

const staticAssets = [  // definir los assets estáticos a "pre-cachear"
	'/sw.js',
	'/static/manifest.webmanifest',
	'/static/base.css',
	'/static/table_resize.js',
	'/static/navbar.js',
	'/static/index.js',
	'/static/checkbox.js',
	'/static/icons/dropIcon.png',


	'https://code.jquery.com/jquery-3.6.0.min.js',
	'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css',
	'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js'
];

const allUserPages = ['/', '/iniciar_sesion', '/offline'];

const allPages = allUserPages.concat([
	'usuarios',
	'puntos_encuentro',
	'zonas_inundables',
	'denuncias',
	'seguimientos',
	'rutas_evacuacion',
	'config'
]);

const allSubpages = [
	'show',
	'nuevo',
	'modify',
	'delete',
	'cerrar_sesion',
	'autenticacion',
	'perfil'
];

// --------------------------------------------------

function networkAndCacheThenCache(event) {
	event.respondWith(
		fetch(event.request)	// en principio se intenta fetchear el dato
		.then(response => {
			return caches.open(cacheName).then(cache => {   // si se consigue se cachea
				cache.put(event.request, response.clone());
				return response;
			});
		})
		.catch(() => {   // si no se puede fetchear se recurre a la cache
			return caches.match(event.request)
			.then(response => {
				return response || offline();
			})
		})
	);
}

function networkOnly(event) {
	event.respondWith(
		fetch(event.request).catch(() => {
			return caches.match('/offline');
		})
	);
}

function cacheThenNetwork(event) {
	event.respondWith(
		caches.match(event.request)
		.then(function(response) {
			return response || fetch(event.request)
			.catch(offline());
		})
	);
}

function offline() {
	return caches.match('/offline');
}

// --------------------------------------------------

const cacheName = 'LPA-cache'; // nombre de la cache a usar

const userPages = fetch('/_allowed_pages')
	.then(response => response.json())
	.then(data => data
		.concat(allUserPages));


self.addEventListener('install', async e => {
	const cache = await caches.open(cacheName);
	await cache.addAll(staticAssets);
	
	userPages.then(data => {
		cache.addAll(data.concat(iconsAssets).concat(mapsAssets));
	});
	
	return self.skipWaiting();
});


self.addEventListener('activate', async e => {
	self.clients.claim();
});

self.addEventListener('fetch', event => {
	let url = event.request.url.split('/');
	let resourceFirst = url.pop();
	let resourceSecond = url.pop();

	let isSubpage = (allSubpages.includes(resourceFirst) || allSubpages.includes(resourceSecond));
	let isPage = allPages.includes(resourceFirst);

	if (isPage || isSubpage) {
		if (isSubpage) networkOnly(event);
		else networkAndCacheThenCache(event);
	} else cacheThenNetwork(event);
});