<template>
  <div class="search-bar">
    <input @keypress.enter="onInput">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      // emit 1. 위로 커스텀 이벤트를 쓴다.
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style scoped>
  div.search-bar {
    text-align: center;
    margin: 20px
  }

  div.search-bar > input {
    width: 75%;
  }
</style>