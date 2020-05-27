<template>
  <div id="app">
    <!-- step 3 : 사용한다. -->
    <MyComponent />
    <!-- <GreatComponent/> -->
  </div>
</template>

<script>
// 컴포넌트 사용하기
// step 1 : import 한다.
import MyComponent from './components/MyComponent.vue'
// import GreatComponent from './components/GreatComponent.vue'

export default {
  name: 'App',
  components: {
    // step 2 : 등록한다.
    MyComponent,
    // GreatComponent,
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
  margin-top: 60px;
}
</style>
