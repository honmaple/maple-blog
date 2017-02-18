// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'
import Header from 'components/common/header'
import filters from './filters'
import globals from './globals'

Vue.use(VueResource);
/* eslint-disable no-new */
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key]);
});
// Object.keys(globals).forEach(key => {
//   Vue.prototype[key] = globals[key];
// });

new Vue({
  el: '#app',
  router:router,
  components: {
    'app-template':App,
    'header-template':Header,
  },
})
