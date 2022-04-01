// workbox.core.setCacheNameDetails({prefix:  "Public-LPA-Cache"});

self.__precacheManifest = [].concat(__precacheManifest || []);

workbox.core.clientsClaim();
self.skipWaiting();

workbox.precaching.precacheAndRoute([{}], {});

// workbox.routing.registerRoute(
//   new RegExp('http://127.0.0.1:5000/api/zonas_inundables/all'),
//   new workbox.strategies.CacheFirst({
//     cacheName: 'workbox',
//     plugins: [
//       new workbox.expiration.Plugin({
//         maxEntries: 30
//       })
//     ],
//     method: 'GET',
//     cacheableResponse: {statuses: [200]}
//   })
// );