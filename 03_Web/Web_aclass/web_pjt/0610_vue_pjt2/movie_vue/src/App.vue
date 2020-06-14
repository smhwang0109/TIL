<template>
  <div id="app">
    <div id="nav">
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login'}">Login</router-link> <span v-if="!isLoggedIn">| </span>
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup'}">Signup</router-link> <span v-if="!isLoggedIn">|</span>
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout'}">Logout</router-link> <span v-if="isLoggedIn">| </span>
      <router-link :to="{ name: 'ArticleList'}">목록으로</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
