# 20200608 TIL

## 오전 라이브 강의

### eventBus

- 모든 component가 eventBus를 통해서 모일 수 있다. 올렸다 내렸다를 왔다갔다를 할 수 있다.



### Vuex

- Vue.js 애플리케이션에 대한 **상태 관리 패턴 + 라이브러리** 입니다.
- **모든 컴포넌트에 대한 중앙 집중식 저장소 역할**을 합니다.
- 언제 사용해야 할까?
  - 공유된 상태 관리를 처리하는 데 유용하지만, 개념에 대한 이해와 시작하는 비용도 합께 듭니다. 단기간과 장기간 생산성 간의 기회비용이 있습니다.
  - 앱이 단순하다면, Vuex 없이도 간단한 글로벌 이벤트 버스로만 괜찮지만,
  - 중대형의 SPA를 구축한다면 Vue 컴포넌트 외부의 상태를 보다 잘 처리할 수 있는 방법을 생각하게 될 가능성이 있으며  Vuex는 자연스럽게 선택할 수 있는 단계가 될 것 입니다.

- 단방향 데이터 흐름 도표
  - ![capture-1580221](images/20200608_TIL/capture-1580221.png)
- 공통의 상태를 공유하는 여러 컴포넌트가 있을 경우, 단순함이 빠르게 저하됩니다.
  - 지나치게 중첩된 컴포넌트를 통과하는 prop는 장황할 수도 있고, 형제 컴포넌트 간에 동작하지 않는다.
  - 또한, 직접 부모/자식 인스턴스를 참조하거나 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화 하려는 등의 해결 방법을 사용해야 합니다.
  - 그래서 Vuex를 사용합니다



### 프로젝트

#### vuex 추가하기

- ```bash
  $ vue add vuex
  ```

- 달라진 점

  - package-lock.json
  - package.json
  - src/main.js
  - src/store



#### index.js

```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // data의 집합(중앙 관리할 모든 데이터 === 상태)
  state: {
  },
  // state를 가공해서 가져올 함수들 === computed
  getters: {},
  // state를 변경하는 함수들 (mutations에 작성되지 않은 state 변경 코드는 모두 동작하지 않습니다.)
  // 모든 mutation 함수들은 동기적으로 동작하는 코드.all
  // commit을 통해 실행합니다.
  mutations: {
  },
  // 범용적인 함수들. mutations에 정의한 함수를 actions에서 실행 가능
  // 비동기 로직은 actions에서 정의.
  // dispatch를 통해 실행함.
  actions: {
  },
  modules: {
  }
})

```



## 오후 12시 Webex 세션

- models.py, serializers.py, views.py 마크다운에 옮겨서 제출하기



## 오후 라이브 강의

### 오늘 배울 일

- DRF를 통해 서버를 만드는 일



### 프로젝트

- ```bash
  $ python -m venv venv
  $ source venv/bin/activate
  $ touch .gitignore
  $ pip install django==2.1.15 djangorestframework
  $ pip freeze > requirements.txt
  $ django-admin startproject django_for_vue .
  $ python manage.py startapp accounts
  $ python manage.py startapp articles
  ```



#### settings.py

- ```python
  INSTALLED_APPS = [
  	'rest_framework',
  	'accounts',
  	'articles',
  ]
  ```



#### accounts/models.py

- ```python
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      pass
  ```

  

#### settings.py

- ```python
  AUTH_USER_MODEL = 'accounts.User'
  ```

  

#### articles/models.py

- ```python
  from django.db import models
  from django.conf import settings
  
  # Create your models here.
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



#### migrate

- ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  

#### articles/serializers.py

- serializers.py 파일 생성

- ```python
  from rest_framework import serializers
  from .models import Article
  
  class ArticleListSerializer(serializers.ModelSerializer):
      class Meta:
          model = Article
          fields = ['id', 'title', 'created_at']
  
  class ArticleSerializer(serializers.ModelSerializer):
      class Meta:
          model = Article
          fields = '__all__'
          
  ```



#### urls.py

- ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ]
  
  ```

  

#### articles/urls.py

> urls.py 파일 생성

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.article_list),
      path('create/', views.create_article),
      path('<int:article_pk>', views.article_detail),
  ]
  ```



#### articles/views.py

- ```python
  from django.shortcuts import get_object_or_404
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .serializers import ArticleListSerializer, ArticleSerializer
  from .models import Article
  
  # Create your views here.
  @api_view(['GET'])
  def article_list(request):
      articles = Article.objects.all()
      serializer = ArticleListSerializer(articles, many=True)
      return Response(serializer.data)
  
  @api_view(['GET'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
  
  @api_view(['POST'])
  def create_article(request):
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
  ```



#### django-rest-auth, djangoallauth install 하기

- ```bash
  $ pip install django-rest-auth django-allauth
  ```

- django-rest-auth: login, logout을 해준다.

- django-rest-auth + django-allauth: signup을 해준다.



#### settings.py

> <a href="https://django-rest-auth.readthedocs.io/en/latest/installation.html">Django-rest-auth Documentation </a>
>
> <a href="https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme">참고문서 - Setting the authentication scheme</a>

- ```python
  INSTALLED_APPS = [
  	#DRF
      'rest_framework',
      'rest_framework.authtoken',
  
      #rest_auth
      'rest_auth'
  ]
  
  
  
  #DRF Auth Settings
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ]
  }
  ```

  - 로그인/로그아웃을 위한 app들을 추가하고, 공식문서의 Setting the authentication scheme 부분에 있는 코드를 복사 붙여넣기 한다.
    - 이때, 우리는 토큰 기반으로 인증을 처리하므로 TokenAuthentication으로 바꿔준다.
  - rest_framework가 인증을 처리하는 방식이 토큰 기반으로 될 것이다.



#### migrate

- ```bash
  $ python manage.py migrate
  ```

- rest_auth 앱이 추가되었으니 migrate를 해야 한다.



#### createsuperuser

- `python manage.py createsuperuser`
- superuser 만들기



#### 회원가입 

##### settings.py

- ```python
  INSTALLED_APPS = [
      'django.contrib.sites',
      'allauth',
      'allauth.account',
      'rest_auth.registration',
  ]
  ```

- allauth, django-rest-auth 관련 앱을 INSTALLED_APPS에 추가한다.



##### migrate

- ```bash
  $ python manage.py migrate
  ```

- 새로운 앱들을 추가했으니 migrate가 필요하다.



##### accounts/serializers.py

- serializers.py 파일 생성

- ```python
  from rest_framework import serializers 
  from .models import Article
  from django.contrib.auth import get_user_model
  
  User = get_user_model()
  
  class UserSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ['id', 'username']
  ```

  - userSerializer와 Articles를 엮는다.



#### article 생성시 user 저장

##### articles/views.py

- ```python
  @api_view(['POST'])
  def create_article(request):
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user) #NOT NULL CONSTRAINT FAILED
          return Response(serializer.data)
  ```

  - `serializer.save(user=request.user)` 를 통해 해당 게시글의 user 저장

- ```python
  from rest_framework.decorators import api_view, permission_classes
  from rest_framework.permissions import IsAuthenticated
  
  @api_view(['POST'])
  @permission_classes([IsAuthenticated])
  def create_article(request):
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user) #NOT NULL CONSTRAINT FAILED
          return Response(serializer.data)
  ```

  - permission_classes, IsAuthenticated 활용한다.
    - 위 decorator를 통해 인증된 사람만 게시글을 생성할 수 있도록 해준다.





## 퀴즈

- Vue) .$emit() 메서드를 사용할 때, 추가 데이터를 넘길 수 없다.:X
- Vue) Vue app을 배포할 때 사용한 서비스 이름을 작성하시오: netlify
- JS) const{name} = student 와 const name = student.name은 같은 코드이다. :X