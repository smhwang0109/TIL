<template>
  <div>
    <p>Videos</p>
    <ul>
      <li v-for="video in videos" :key="video.etag">
        <img :src="video.snippet.thumbnails.default.url" alt="">
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name:'VideoList',
  props: {
    videos: Array,
  }
}
</script>

<style>

</style>