import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue'
import MoviesView from '../views/MoviesView.vue'
import AboutView from '../views/AboutView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
      component: AboutView
    },
    {
      path: '/movies/create',
      name: 'create',
      // component: () => import('../views/AddMovieFormView.vue')
      component: AddMovieFormView
      
    },
    {
      path: '/movies',
      name: 'movies',
      // component: () => import('../views/MoviesView.vue')
      component: MoviesView
    }

  ]
})

export default router
