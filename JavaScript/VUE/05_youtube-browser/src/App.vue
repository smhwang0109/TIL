<template>
  <div class="container">
    <!-- emit 듣고 함수 실행 -->
    <div class="row">
      <SearchBar @input-change="onInputChange"/>
    </div>
    <div class="row">
      <div class="col-9">
        <VideoPlay :video="video"/>
      </div>
      <div class="col-3">
        <VideoList :videos="videos"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios  from 'axios'

import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoPlay from './components/VideoPlay.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoPlay,
  },
  data() {
    return {
      inputValue: '',
      video: {},
      videos: [],
    }
  },
  methods: {
    onInputChange(value) {
      this.inputValue = value
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue,
          maxResults: 5
        }
      })
        .then(res => {
          this.video = res.data.items[0]
          this.videos = res.data.items.slice(1)
        })
        .catch(err => console.error(err))
    }
  }
}
</script>

<style>
</style>
