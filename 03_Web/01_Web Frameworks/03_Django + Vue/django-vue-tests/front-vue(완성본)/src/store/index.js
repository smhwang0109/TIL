import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import axios from 'axios'

import router from '@/router'
import SERVER from '@/api/drf'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    articles: [],
  },
  getters: {
    isLoggedIn : state => !!state.authToken,
    config: state => ({headers: {Authorization: `Token ${state.authToken}`}})
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    // postAuthData(context, info) {
    postAuthData({ commit }, info) { // context에서 commit만 쓰겠다.
      axios.post(SERVER.URL + info.location, info.data)
        .then(res => {
          // context.commit('SET_TOKEN', res.data)
          commit('SET_TOKEN', res.data.key)
          router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup
      }
      dispatch('postAuthData', info) // actions는 dispatch로 실행하고 인자는 하나만 넘길 수 있어서 info로 묶어서 넘긴다.
    },
    
    login({ dispatch }, loginData) { 
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login
      }
      dispatch('postAuthData', info)
    },

    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => { // Django DB에서는 삭제 | cookie, state에는 남아있음
          commit('SET_TOKEN', null) // state에서 삭제
          cookies.remove('auth-token') // cookie에서 삭제
          router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },

    fetchArticles({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.aritcleList)
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err))
    },

    createArticle({ getters }, articleData) {
      axios.post(SERVER.URL + SERVER.ROUTES.createArticle, articleData, getters.config)
        .then(() => {
          this.$router.push({ name: 'List' })
        })
        .catch(err => console.log(err.response.data))
    },
  },
  modules: {
  }
})
