import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import titleMixin from './router/titleMixin'
import PrimeVue from 'primevue/config'
import 'bootstrap'


import 'primevue/resources/themes/mdc-light-indigo/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons


const app = createApp(App)

app.use(router)
app.use(PrimeVue)
app.mixin(titleMixin)

app.mount('#app')
