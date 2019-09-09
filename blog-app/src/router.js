import Vue from 'vue'
import Router from 'vue-router'
import defaultPage from '@/layout/default'
import Index from '@/views/Index.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'defaultPage',
      redirect: '/index',
      component: defaultPage,
      children: [
        {
          path: 'index',
          name: 'index',
          component: Index
        },
        {
          path: '/',
          redirect: '/index',
          name: 'defaultBody',
          component: () => import('./layout/defaultBody.vue'),
          children: [
            {
              path: 'about',
              name: 'about',
              component: () => import('./views/About.vue')
            },
            {
              path: 'archives',
              name: 'archives',
              component: () => import('./views/Archives.vue')
            },
            {
              path: 'article/:id',
              name: 'article',
              component: () => import('./views/Article.vue')
            },
            {
              path: 'friends',
              name: 'friends',
              component: () => import('./views/Friends.vue')
            },
            {
              path: 'messages',
              name: 'messages',
              component: () => import('./views/Messages.vue')
            }
          ]
        }
      ]
    },
    
  ]
})
