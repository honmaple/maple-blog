// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'
import Header from 'components/common/header'
import * as filters from './filters'

Vue.use(VueResource);
/* eslint-disable no-new */
Object.keys(filters).forEach(key => {
    Vue.filter(key, filters[key])
})
new Vue({
    el: '#app',
    router,
    components: {
        'app-template':App,
        'header-template':Header,
    },
})
