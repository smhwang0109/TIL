<template>
  <div class="container d-flex flex-column align-items-center">
    <button class="btn text-light bg-dark"><router-link :to="{ name: 'ArticleCreate' }">글쓰기</router-link></button>
    <br>
    <h1>
      커뮤니티
    </h1>
    <form class="d-flex flex-column">
      <div class="form-group">
        <label for="title">Title</label>
        <input v-model="articleData.title" type="text" class="form-control" id="title">
        <small id="title" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요.</small>
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea v-model="articleData.content" class="form-control" id="content" cols="50" rows="10"></textarea>
      </div>
      <button @click="createArticle(articleData)" class="btn btn-primary">작성하기</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      articleData: {
        title: null,
        content: null
      }
    }
  },
  methods: {
    ...mapActions(['createArticle'])
  }
}
</script>

<style>

</style>