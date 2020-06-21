import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'

import CreateView from '@/views/articles/CreateView.vue'
import ListView from '@/views/articles/ListView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView,
  },
  {
    path: '/articles/create',
    name: 'Create',
    component: CreateView,
    // beforeEnter(from, to, next) {
    //   console.log(from, to)
    //   if (!Vue.$cookies.isKey('auth-token')) {
    //     next('/accounts/login')
    //   } else {
    //     next()
    //   }
    // }
  },
  {
    path: '/articles',
    name: 'List',
    component: ListView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const pubicPages = ['Login', 'Signup', 'Home', 'List'] // Login 안해도 됨
  const authPages = ['Login', 'Signup'] // Login 되어있으면 안됨
  const authRequired = !pubicPages.includes(to.name) // 로그인 해야하는 페이지면 true 반환
  const unauthRequired = authPages.includes(to.name)
  const isLoggedIn = Vue.$cookies.isKey('auth-token')

  if (unauthRequired && isLoggedIn){
    next('/')
  }

  authRequired && !isLoggedIn ? next({ name:'Login' }) : next()
  // if (authRequired && !isLoggedIn) {
  //   next({ name: 'Login' })
  // } else {
  //   next()
  // }

})

export default router
