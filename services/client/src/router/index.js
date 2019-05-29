import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Models from '@/views/Models';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Models',
      component: Models,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
