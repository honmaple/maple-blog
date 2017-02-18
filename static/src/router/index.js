import Vue from 'vue'
import Router from 'vue-router'
import Index from 'components/index'
import About from 'components/about'
import Friend from 'components/friend'
import BlogHeader from 'components/blog/base'
import BlogList from 'components/blog/itemlist'
import Blog from 'components/blog/item'
import BookHeader from 'components/book/base'
import BookList from 'components/book/itemlist'
import Book from 'components/book/item'
import TimeLineHeader from 'components/timeline/base'
import TimeLineList from 'components/timeline/itemlist'


Vue.use(Router)

export default new Router({
  // mode:'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/friends',
      name: 'friend',
      component: Friend
    },
    {
      path: '/blog',
      component: BlogHeader,
      children: [
        {
          path: '',
          name: 'bloglist',
          component: BlogList
        },
        {
          path: ':blogId',
          name: 'blog',
          component: Blog,
        }]
    },
    {
      path: '/book',
      component: BookHeader,
      children: [
        {
          path: '',
          name: 'booklist',
          component: BookList
        },
        {
          path: ':bookId',
          name: 'book',
          component: Book
        }]
    },
    {
      path: '/timeline',
      component: TimeLineHeader,
      children: [{
        path: '',
        name: 'timelinelist',
        component: TimeLineList
      }]
    },
    {
      path: '/question',
      component: BlogHeader,
      children: [
        {
          path: '',
          name: 'questionlist',
          component: BlogList
        },
        {
          path: ':questionId',
          name: 'question',
          component: Blog
        }]
    }
  ]
})
