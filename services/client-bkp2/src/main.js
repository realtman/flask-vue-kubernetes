import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VueCookies from 'vue-cookies'
import App from './App';
import router from './router';

import 'bootstrap/dist/css/bootstrap.css';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(VueCookies);

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>',
// });
new Vue({
    router: router,
    render: h => h(App),

}).$mount('#app');
