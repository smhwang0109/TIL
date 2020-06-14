import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // data의 집합(중앙 관리할 모든 데이터 === 상태)
  state: {
    inputValue: '',
    videos: [],
    selectedVideo: null,
  },
  // state를 (가공해서) 가져올 함수들. === computed
  getters: {
    videoUrl(state) {
      return `https://www.youtube.com/embed/${state.selectedVideo.id.videoId}`
    },
    videoTitle: state => state.selectedVideo.snippet.title,
    videoDescription: state => state.selectedVideo.snippet.description
  },
  // state를 변경하는 함수들(mutations에 작성되지 않은 state 변경 코드는 모두 동작하지 않음.)
  // 모든 mutation 함수들은 동기적으로 동작하는 코드.all
  // commit을 통해 실행함.
  mutations: {
    setInputValue(state, inputValue) {
      state.inputValue = event.target.value
    },
    setVideos(state) {
      console.log(state)

    },
    setSelectedVideo(state, video) {
      state.selectedVideo = video
    }
  },
  // 범용적인 함수들. mutations에 정의한 함수를 actions에서 실행 가능.
  // 비동기 로직은 actions에서 정의.
  // dispatch를 통해 실행함
  actions: {
    fetchVideos(context, event) {
      // 1. inputValue를 바꾼다.
      context.commit('setInputValue', event.target.)
      // 2. state.inputValue로 요청 보낸다.

      // 3. state.videos 를 응답으로 바꾼다.
    } 
  },
  modules: {
  }
})
