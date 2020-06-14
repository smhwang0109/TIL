<template>
  <div class="parent">
    <h1>부모 컴포넌트</h1>
    <!-- 1. prop 이름="내용" -->
    <Child @hungry="sendHungrySignal" :propFromParent="parentMsg"/>
  </div>
</template>

<script>
import Child from '../components/Child.vue'

export default {
  name: "Parent",
  data() {
    return{
      parentMsg: '부모에서 보낸 메시지',
    }
  },
  components: {
    // 'Child': Child,
    // 이걸 줄여서 이렇게 작성
    Child
  },
  methods: {
    sendHungrySignal(menu1, menu2) {
      this.parentMsg = `${menu1}, ${menu2} 먹어라`
    }
  }
};
</script>

<style>
  .parent {
    border: 3px solid red;
    margin: 3px;
    padding: 3px;
  }
</style>