window.addEventListener('load', () => {
  if (!('fetch' in window)) {
    console.log('La Fetch API no fue encontrada, por favor actualice su navegador.');
    return;
  }
  // Desde este punto en adelante se puede usar fetch de manera segura
  registerSW();
});

async function registerSW() {
  if ('serviceWorker' in navigator) {
    try {
      await navigator.serviceWorker.register('/sw.js').then(registration => {
        console.log('Service worker registrado en', registration.scope);
      })
    } catch (e) {
      console.error('Error al registrar el service worker:', e);
    }
  }
}