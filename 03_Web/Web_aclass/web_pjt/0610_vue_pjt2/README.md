# :clapper: Vue Project

## 프로젝트 소개

### 👩‍💻🧑‍💻 프로젝트 멤버

- 황수민
- 박선환



### 💻 기술 스택

- | Framework | 라이브러리            |
  | --------- | --------------------- |
  | Django    | django-allauth        |
  |           | django-rest-framework |
  |           | django-rest-auth      |
  |           | django-cors-headers   |
  | Vue.js    | axios                 |
  |           | vue-cookies           |
  |           | Bootstrap             |



### 📂 컴포넌트 구조

│  .gitignore
│  README.md
│  
├─movie_api
│  │  manage.py
│  │  README.md
│  │  requirements.txt
│  │  
│  ├─accounts
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  serializers.py
│  │  │  tests.py
│  │  │  views.py
│  │  │  __init__.py
│  │  │  
│  │  ├─migrations
│  │  │  │  0001_initial.py
│  │  │  │  __init__.py
│  │  │          
│  │          
│  ├─articleBack
│  │  │  settings.py
│  │  │  urls.py
│  │  │  wsgi.py
│  │  │  __init__.py
│  │          
│  ├─articles
│  │  │  admin.py
│  │  │  apps.py
│  │  │  models.py
│  │  │  serializers.py
│  │  │  tests.py
│  │  │  urls.py
│  │  │  views.py
│  │  │  __init__.py
│  │  │  
│  │  ├─migrations
│  │  │  │  0001_initial.py
│  │  │  │  __init__.py
│  │          
│  └─venv
│                  
└─movie_vue
    │  babel.config.js
    │  package-lock.json
    │  package.json
    │  README.md
    │  
    ├─node_modules
    │              
    ├─public
    │      favicon.ico
    │      index.html
    │      
    └─src
        │  App.vue
        │  main.js
        │  
        ├─api
        │      drf.js
        │      
        ├─assets
        ├─components
        ├─router
        │      index.js
        │      
        ├─store
        │      index.js
        │      
        └─views
            ├─accounts
            │      LoginView.vue
            │      LogoutView.vue
            │      SignupView.vue
            │      
            └─articles
                    ArticleCreateView.vue
                    ArticleListView.vue



### 📌 기능

- 회원 관련 기능
  - 로그인
    - 토큰 기반 인증으로 진행, 쿠키에 저장하여 활용
  - 회원가입
  - 로그아웃
- 게시판 기능
  - 게시글 생성
  - 게시글 목록 조회



## Discussion

- 시작부터 vuex
- src 파일 아래 api/drf.js를 만들어 drf관련 정보 저장
- Convention 맞추기
  - import 할 때 src 폴더를 `@`로 통일



## 구현 과정

### ⚙Django 초기 설정

#### pip install

- ```bash
  $ pip install -r requirements.txt
  ```



#### CORS header 설정

- ```python
  # settings.py
  
  INSTALLED_APPS = [
      # CORS
      'corsheaders',
  ]
  
  MIDDLEWARE = [
      'corsheaders.middleware.CorsMiddleware',
      # ... 순서
      'django.middleware.common.CommonMiddleware',
  ]
  
  # CORS Allow
  CORS_ORIGIN_ALLOW_ALL = True
  ```



### ⚙Vue 초기 설정

#### 라우터/vuex 추가

- ```bash
  $ vue add router
  $ vue add vuex
  ```
```
  



#### 라이브러리 추가

- ```bash
  $ npm i axios
  $ npm i vue-cookies
```



#### 컴포넌트 생성

- 사용할 컴포넌트를 모두 생성하였습니다. 



#### 폴더 구조 

- `views`폴더 안에 컴포넌트들을 기능에 따라  `accounts`, `articles`로 분리



#### `public/index.html` Bootstrap 추가

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title><%= htmlWebpackPlugin.options.title %></title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>

```





#### `router/index.js` 추가

- 1. `index.js` 파일에 컴포넌트들을 import 시켰습니다.
- 2. routes에 path, name, component를 설정하였습니다.

```js
import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'

import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import ArticleListView from '@/views/articles/ArticleListView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/articles/',
    name: 'ArticleList',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreate',
    component: ArticleCreateView
  }
]
```



### Vuex

#### src/store/index.js

```js
import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import axios from 'axios'

import router from '@/router'
import SERVER from '@/api/drf'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 저장된 데이터들
    authToken: cookies.get('auth-token'),
    articles: []
  },
  getters: {
    // 로그인 상태 확인
    isLoggedIn: state => !!state.authToken,
    
    // headers 저장
    config: state => ({ headers: { Authorization: `Token ${state.authToken}`}})
  },
  mutations: {
    // 토큰 변경
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
      
    // 게시글들
    SET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    // Login/Signup 해주는 함수
    postAuthData({ commit }, info) {
      axios.post(SERVER.URL + info.location, info.data)
        .then(res => {
          commit('SET_TOKEN', res.data.key)
          router.push({ name: 'ArticleList' })
        })
        .catch(err => console.log(err.response.data))
    },
      
    // 회원가입
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup
      }
      dispatch('postAuthData', info)
    },
      
    // 로그인
    login({ dispatch }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login
      }
      dispatch('postAuthData', info)
    },
      
    // 로그아웃
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          commit('SET_TOKEN', null)
          cookies.remove('auth-token')
          router.push({ name: 'ArticleList'})
        })
        .catch(err => console.log(err.response.data))
    },
      
    // 게시글 가져오기
    fetchArticles({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.articleList)
        .then(res => {
          commit('SET_ARTICLES', res.data)
        })
        .catch(err => console.log(err.response.data))
    },
    
    // 게시글 작성
    createArticle({ getters }, articleData) {
      axios.post(SERVER.URL + SERVER.ROUTES.createArticle, articleData, getters.config)
        .then(() => {
          router.push({ name: 'ArticleList'})
        })
        .catch(err => console.log(err.response.data))
    }
  },
  modules: {
  }
})
```





### App.vue

#### Getters를 이용해 로그인 된 상태 확인

```vue
<template>
  <div id="app">
    <div id="nav">
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login'}">Login</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup'}">Signup</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout'}">Logout</router-link> |
      <router-link :to="{ name: 'ArticleList'}">목록으로</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

```





### Accounts

#### LoginView.vue

##### Actions 사용해 로그인

```vue
<template>
  <div class="container">
    <h1>로그인</h1>
    <div class="form-group">
      <label for="username">username</label>
      <input class="form-control" v-model="loginData.username" id="username" type="text">
    </div>
    <div class="form-group">
      <label for="password">password</label>
      <input class="form-control" v-model="loginData.password" id="password" type="password">
    </div>
    <button @click="login(loginData)" class="btn btn-primary">Login</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>
```



#### SignupView.vue

##### Actions 사용해 회원가입

```vue
<template>
  <div class="container">
    <h1>로그인</h1>
    <div class="form-group">
      <label for="username">username</label>
      <input class="form-control" v-model="loginData.username" id="username" type="text">
    </div>
    <div class="form-group">
      <label for="password">password</label>
      <input class="form-control" v-model="loginData.password" id="password" type="password">
    </div>
    <button @click="login(loginData)" class="btn btn-primary">Login</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>
```



#### LogoutView.vue

##### Actions 사용해 로그아웃

- 컴포넌트를 새로 만들어서, 라우팅 뿐만 아니라 created를 이용해 url을 통해서도 로그아웃이 가능하도록 구현 

```vue
<template>
  <div></div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LogoutView',
  methods: {
    ...mapActions(['logout'])
  },
  created(){
    this.logout()
  }
}
</script>
```



### Accounts

#### ArticleListView.vue

##### State, Actions를 사용해 게시글 불러오기

```vue
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
```



#### ArticleCreateView.vue

##### Actions를 사용해 게시글 작성

```vue
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
```



##### ❗️ 어려웠던 점

- 기존에 form 태그로 감쌌을 때 페이지가 새롭게 랜더되는 문제 발생
- form 태그를 없앴을 때, created_at이 필수요소라는 에러 발생
- created_at이 필수요소가 아닐 때, 한글 인코딩 문제 발생

##### :star: 해결

- form 태그를 삭제하였습니다.

- movie_api(장고파트)에 Serializers.py 에 created_at의 포멧을 정해놓은 문제

- ```python
  class ArticleSerializer(serializers.ModelSerializer):
      user = UserSerializer(required=False)
      # created_at = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S")
      created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
  
      class Meta:
          model = Article
          fields = '__all__'
          read_only_fields = ('id', 'user', 'created_at', 'updated_at')
  
  ```

- 필수요소가 아니도록 만들기 위해 `required=False` 추가

- 한글 인코딩 문제 해결하기 위해 인코딩, 디코딩 후 다시 인코딩, 디코딩을 하는 과정을 생략하기 위해 `-` 삽입



### Router

#### router/index.js

##### 로그인 상태에 따른 페이지 설정 추가

```js
// ...

router.beforeEach((to, from, next) => {
  const publicPages = ['Login', 'Signup', 'ArticleList']
  const authPages = ['Login', 'Signup']
  const authRequired = !publicPages.includes(to.name)
  const unauthRequired = authPages.includes(to.name)
  const isLoggedIn = Vue.$cookies.isKey('auth-token')

  if (unauthRequired && isLoggedIn) {
    next({ name: 'ArticleList' })
  }

  if (authRequired && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})
```





## 구현 화면

### 메인 화면(글 목록)

![메인화면](images\메인화면.JPG)



### 로그인 화면

![로그인](images\로그인.JPG)



### 로그인 후

![로그인 후](images\로그인 후.JPG)



### 글작성

![글작성](images\글작성.JPG)





### 회원가입

![회원가입](images\회원가입.JPG)

<br>

## 느낀점

- 컴포넌트와 js 등 파일들이 많아지다 보니 오타를 찾기가 쉽지 않아, 자주 테스트를 해보며 개발 해야겠다 생각했습니다.

- vuex를 처음부터 작성해보면서 전체적인 체계를 직접 만들어보며 익숙해질 수 있어 좋았습니다.

