<template>
  <div class="container d-flex flex-column align-items-center">
    <button class="btn text-light bg-dark"><router-link :to="{ name: 'ArticleCreate' }">글쓰기</router-link></button>
    <br>
    <h1>
      게시판
    </h1>
    <table class="table">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="`article_${article.id}`">
          <th scope="row">{{ article.id }}</th>
          <td>{{ article.title }}</td>
          <td>{{ article.user.username }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ArticleListView',
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>