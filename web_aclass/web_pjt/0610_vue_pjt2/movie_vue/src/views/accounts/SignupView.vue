<template>
  <div class="container">
    <h1>회원가입</h1>
    <div class="form-group">
      <label for="username">username</label>
      <input class="form-control" v-model="signupData.username" id="username" type="text">
    </div>
    <div class="form-group">
      <label for="password1">password</label>
      <input class="form-control" v-model="signupData.password1" id="password1" type="password">
    </div>
    <div class="form-group">
      <label for="password2">password-confirm</label>
      <input class="form-control" v-model="signupData.password2" id="password2" type="password">
    </div>
    <button @click="signup(signupData)" class="btn btn-primary">Signup</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'SignupView',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>