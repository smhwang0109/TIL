<template>
  <div>
    <h1>Login</h1>
    username: <input type="text" v-model="loginData.username">
    password: <input type="password" v-model="loginData.password">
    <button @click="login">Login</button>
  </div>
</template>

<script>
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
    login() {
      this.$emit('submit-login-data', this.loginData)
    }
  }
}
</script>

<style>

</style>