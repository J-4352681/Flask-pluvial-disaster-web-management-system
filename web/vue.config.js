module.exports = {
  pwa: {
    name: 'La Plata Agua',
    themeColor: 'white',
    appleMobileWebAppStatusBarStyle: 'white',
    id: 'LPA',
    workboxPluginMode: 'InjectManifest',
    workboxOptions: {
      swSrc: 'src/service-worker.js'
    }
  }
}