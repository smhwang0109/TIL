import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'

import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import ArticleListView from '@/views/articles/ArticleListView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/articles/',
    name: 'ArticleList',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreateView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Login', 'Signup', 'ArticleList']
  const authPages = ['Login', 'Signup']
  const authRequired = !publicPages.includes(to.name)
  const unauthRequired = authPages.includes(to.name)
  const isLoggedIn = Vue.$cookies.isKey('auth-token')

  if (unauthRequired && isLoggedIn) {
    next({ name: 'ArticleList' })
  }

  if (authRequired && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
