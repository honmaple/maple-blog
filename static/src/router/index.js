import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

function lazyload(name) {
  return function(resolve) {
    require(['components/' + name + '.vue'], resolve);
  };
}

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      components: {
        default:{
          template:'<router-view></router-view>'
        },
        header:lazyload('common/header')
      },
      children: [
        {
          path: '',
          name: 'index',
          component: lazyload('index')
        },
        {
          path: 'about',
          name: 'about',
          component: lazyload('about')
        },
        {
          path: 'friends',
          name: 'friend',
          component:lazyload('friend')
        }
      ]
    },
    {
      path: '/blog',
      components: {
        default:lazyload('blog/base'),
        header:lazyload('blog/header')
      },
      children: [
        {
          path: '',
          name: 'bloglist',
          component: lazyload('blog/itemlist')
        },
        {
          path: 'archives',
          name: 'blogarchives',
          component: lazyload('blog/archives')
        },
        {
          path: ':blogId',
          name: 'blog',
          component: lazyload('blog/item')
        },
      ]
    },
    {
      path: '/books',
      components: {
        default:lazyload('book/base'),
        header:lazyload('book/header')
      },
      children: [
        {
          path: '',
          name: 'booklist',
          component: lazyload('book/itemlist')
        },
        {
          path: ':bookId',
          name: 'book',
          component: lazyload('book/item')
        }]
    },
    {
      path: '/timeline',
      components: {
        default:lazyload('timeline/base'),
        header:lazyload('common/header')
      },
      children: [{
        path: '',
        name: 'timelinelist',
        component: lazyload('timeline/itemlist')
      }]
    },
    {
      path: '/',
      components: {
        default:lazyload('pages/base'),
        header:lazyload('common/header')
      },
      children: [
        {
          path: '403',
          name: '403',
          component: lazyload('pages/403')
        },
        {
          path: '404',
          name: '404',
          component: lazyload('pages/404')
        },
        {
          path: '500',
          name: '500',
          component: lazyload('pages/500')
        }
      ]
    },
    {
      path:'*',
      components: {
        default:lazyload('pages/404'),
        header:lazyload('common/header')
      }
    }
  ],
  scrollBehavior: function(to, from, savedPosition) {
    if (to.hash) {
      return {
        selector: to.hash
      };
    }
    return { x: 0, y: 0 };// return 期望滚动到哪个的位置
  }
});
