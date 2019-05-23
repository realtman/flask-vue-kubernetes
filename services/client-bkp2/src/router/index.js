import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/views/Ping';
import Models from '@/views/Models';
import CCDView from '@/views/CCD.vue'
import JobListView from '@/views/JobList.vue'
import JobCreateComponent from '@/components/JobCreate.vue'
import JobStatusComponent from '@/components/JobStatus.vue'
import RestApiExampleView from '@/views/RestApiExample.vue'

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
    {
      path: '/ccd',
      name: 'CCDView',
      component: CCDView,
    },
    {
      path: '/job-list',
      name: 'JobListView',
      component: JobListView,
    },
    {
      path: '/job-create',
      name: 'JobCreateComponent',
      component: JobCreateComponent,
    },
    {
      path: '/job-status/:jobId',
      name: 'JobStatusComponent',
      component: JobStatusComponent,
    },
    {
      path: '/demo-restapi',
      name: 'RestApiExampleView',
      component: RestApiExampleView,
    },
  ],
  // mode: 'history',
  mode: 'hash',
});
