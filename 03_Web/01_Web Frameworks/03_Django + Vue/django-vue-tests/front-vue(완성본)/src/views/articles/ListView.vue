<template>
  <div>
    <h1>Article List</h1>
    <ul>
      <li v-for="article in articles" :key="`article_${article.id}`">
        {{ article.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "ListView",
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
};
</script>

<style>
</style>