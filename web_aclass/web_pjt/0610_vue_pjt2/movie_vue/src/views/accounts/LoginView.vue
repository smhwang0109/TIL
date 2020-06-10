<template>
  <div class="container">
    <h1>로그인</h1>
    <div class="form-group">
      <label for="username">username</label>
      <input class="form-control" v-model="loginData.username" id="username" type="text">
    </div>
    <div class="form-group">
      <label for="password">password</label>
      <input class="form-control" v-model="loginData.password" id="password" type="password">
    </div>
    <button @click="login(loginData)" class="btn btn-primary">Login</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>