self.__precacheManifest = [].concat(__precacheManifest || []);

// let regex;
// if (process.env.NODE_ENV === 'production') {
//   regex = /https:\/\/admin-grupo38\.proyecto2021\.linti\.unlp\.edu\.ar\/api\/.*/
// } else {
//   regex = /https:\/\/127\.0\.0\.1:5000\/api\/.*/
// }

workbox.core.clientsClaim();
workbox.core.skipWaiting();

workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

workbox.routing.registerRoute(
  /https:\/\/127\.0\.0\.1:5000\/api\/.*/,
  workbox.strategies.networkFirst({
    cacheName: 'apis',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 días
      })
    ]
  })
);

let click_open_url;

self.addEventListener('push', event => {
  let push_message = event.data.text();
  click_open_url = '/';
  const options = {
    body: push_message,
    icon: './img/icons/android-chrome-192x192.png',
    vibrate: [200, 100, 200, 100, 200, 100],
    tag: 'Nueva información en el sistema'
  };
  event.waitUntil(
    self.registration.showNotification('Nueva información en LPA', options)
  );
});

self.addEventListener('notificationclick', event => {
  const clickedNotification = event.notification;
  clickedNotification.close();
  if (click_open_url) {
    const promiseChain = clients.openWindow(click_open_url);
    event.waitUntil(promiseChain);
  }
});