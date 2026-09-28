import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import Analyze from '@/views/Analyze.vue'
import History from '@/views/History.vue'
import About from '@/views/About.vue'

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/analyze',
      name: 'Analyze',
      component: Analyze
    },
    {
      path: '/history',
      name: 'History',
      component: History
    },
    {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})

export default router