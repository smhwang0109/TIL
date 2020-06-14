# 20200413 TIL

## 오전 라이브 강의

### 오늘 배울 내용 소개

- `admin.py`에서 `list_display`, `list_display_links`, `list_filter`
- Message Framework

<br>

### 인스타그램 클론코딩 (기초)

#### 프로젝트 만들기

- ```bash
  $ django-admin startproject instagram
  ```

<br>

#### 깃 설정

- ```bash
  $ git init
  ```

##### gitignore 파일 만들기: 특정 파일을 내가 git으로 관리하지 않겠다.

- db.sqlite3: db파일은 git으로 관리하지 않는다.

- gitignore.io에서 django라고 설정하면 나오는 content를 .gitignore파일에 추가한다.

- ```
  # Created by https://www.gitignore.io/api/django
  # Edit at https://www.gitignore.io/?templates=django
  
  ### Django ###
  *.log
  *.pot
  *.pyc
  __pycache__/
  local_settings.py
  db.sqlite3
  db.sqlite3-journal
  media
  
  # If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/
  # in your Git repository. Update and uncomment the following line accordingly.
  # <django-project-name>/staticfiles/
  
  ### Django.Python Stack ###
  # Byte-compiled / optimized / DLL files
  *.py[cod]
  *$py.class
  
  # C extensions
  *.so
  
  # Distribution / packaging
  .Python
  build/
  develop-eggs/
  dist/
  downloads/
  eggs/
  .eggs/
  lib/
  lib64/
  parts/
  sdist/
  var/
  wheels/
  pip-wheel-metadata/
  share/python-wheels/
  *.egg-info/
  .installed.cfg
  *.egg
  MANIFEST
  
  # PyInstaller
  #  Usually these files are written by a python script from a template
  #  before PyInstaller builds the exe, so as to inject date/other infos into it.
  *.manifest
  *.spec
  
  # Installer logs
  pip-log.txt
  pip-delete-this-directory.txt
  
  # Unit test / coverage reports
  htmlcov/
  .tox/
  .nox/
  .coverage
  .coverage.*
  .cache
  nosetests.xml
  coverage.xml
  *.cover
  .hypothesis/
  .pytest_cache/
  
  # Translations
  *.mo
  
  # Scrapy stuff:
  .scrapy
  
  # Sphinx documentation
  docs/_build/
  
  # PyBuilder
  target/
  
  # pyenv
  .python-version
  
  # pipenv
  #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
  #   However, in case of collaboration, if having platform-specific dependencies or dependencies
  #   having no cross-platform support, pipenv may install dependencies that don't work, or not
  #   install all needed dependencies.
  #Pipfile.lock
  
  # celery beat schedule file
  celerybeat-schedule
  
  # SageMath parsed files
  *.sage.py
  
  # Spyder project settings
  .spyderproject
  .spyproject
  
  # Rope project settings
  .ropeproject
  
  # Mr Developer
  .mr.developer.cfg
  .project
  .pydevproject
  
  # mkdocs documentation
  /site
  
  # mypy
  .mypy_cache/
  .dmypy.json
  dmypy.json
  
  # Pyre type checker
  .pyre/
  
  # End of https://www.gitignore.io/api/django
  ```

<br>

#### 장고 초기 설정

- settings.py

  - ```python
    ALLOWED_HOSTS = ['*']
    LANGUAGE_CODE = 'ko_kr'
    TIME_ZONE = 'Asia/Seoul'
    ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m "Init Instagram project with .gitignore"
  ```

<br>

#### 앱 생성 

- ```bash
  $ python manage.py startapp articles
  ```

  - 작성할 때 **앱 이름은 반드시 복수형!**!!
  - **모델은 반드시 단수형**!!

<br>

#### 앱 설정

- settings.py

  - ```python
    INSTALLED_APPS = [
    	'articles',
    ]
    ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m "Init articles app"
  ```

<br>

#### 모델 설정

- ```python
  from django.db import models
  
  class Article(models.Model):
  	title = models.CharField(max_length=100)
      content = models.TestField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- ```bash
  $ python manage.py showmigrations 
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

<br>

#### 어드민 설정

> 어떠한 모델에 대한 내용을 관리자로 관리하고 싶다.

##### import 작성순서

- python core (random, os)

- django (from django.contrib, from django.urls 등)

- 내가 만든 모델, url등

  

##### admin.py

- ```python
  from django.contrib import admin
  from .models import Article
  
  #Register your models here
  admin.site.register(Article)
  ```
  - admin.py를 작성하는 이유: 어떠한 모델에 대한 내용을 관리하고 싶다.

  - 현재 경로에 있는 Article 모델을 가져온다.

    - ```python
      from .models import Article
      ```

- 위 등록방법을 확장해서 만들고 싶다면?

  - ```python
    class ArticleAdmin(admin.ModelAdmin):
    	list_display=['id', 'title', 'created_at', 'updated_at']
        list_display_links=['title']
        list_filter=['created_at']
    admin.site.register(Article, ArticleAdmin)
    ```

  - `list_display`는 어드민 페이지에 보여주기 위한 설정이다.

  - `list_display_links`는 id가 아닌 제목을 눌렀을 때 상세 게시글로 들어가기가 가능하다.

  - `list_filter`: created_at을 기준을 게시글을 볼 수 있다 (언제나, 오늘, 지난7일, 이번달, 이번해)

- 관리자 만들기

  - ```bash
    $ python manage.py createsuperuser
    ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m 'Create Article Model'
  ```

<br>

#### forms.py

- ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = '__all__'
  ```

  - class Meta: 어떠한 모델에 어떠한 필드를 Form으로 보여준다는 것이기 때문에 두가지 설정을 보여줘야 한다.

<br>

#### urls 설정

##### 프로젝트폴더/urls.py	

- ```python
  from django.contrib import admin
  from django.urls import path, include
  urlpatterns = [
  	path('admin/', admin.site.urls),
  	path('articles/', include('articles.urls'))
  ]
  ```

##### articles/urls.py

- ```python
  from django.urls import path 
  urlpatterns = [
  ]
  ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit --amend #커밋을 묶어서 했다
  ```

<br>

#### index 페이지 만들기 (목록페이지)

##### urls.py

- ```python
  from django.urls import path 
  from . import views
  urlpatterns = [
  	path('', views.index),
  ]
  ```

  

##### views.py

- ```python
  from django.shortcuts import render
  from .models import Article
  
  def index(request):
  	articles = Article.object.order_by('-pk') #최근 글들이 더 위로 올라온다.
      #articles= Article.object.order_by('created_at')
      context = {
          'articles':articles
      }
      return render(request, 'articles/index.html', context)
  ```

<br>

#### templates 폴더 구조 설정

- articles 앱 내에 templates 폴더 추가, 그 폴더 안에 articles 폴더 추가, 그 안에 `index.html` 추가

<br>

#### index.html (article 출력)

- ```html
  {% for article in articles %}
  	<p>{{ article.pk }}</p>
  {% endfor %}
  ```

<br>

##### urls.py에 app_name 설정과 url 별로 name 설정

- ```python
  from django.urls import path 
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
  	path('', views.index, name='index'),
  ]
  ```

  - 나중에 url이 변경되어도 미리 변수화를 해놓고, 실제 변수화를 했을 때, 나중에 url을 변경되더라도 실제 html코드나 views.py 코드를 변경하지 않기 위해서 name을 설정해준다.

<br>

#### base.html추가

##### settings.py

- ```python
  Templates = [
      {
          'DIRS': [
              os.path.join(BASE_DIR, 'templates')
          ]
      }
  ]
  ```

##### 폴더 구조 설정

- BASE_DIR에 templates 폴더를 추가하고, 그 안에 base.html 추가

##### base.html

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Instagram</title>
      {% block css %}
      {% endblock %}
  </head>
  <body>
      {% block body %}
      {% endblock %}
  </body>
  </html>
  ```

<br>

#### index.html (block 추가)

- ```html
  {% extends 'base.html' %}
  
  {% block title %}목록 {% endblock %}
  {% block body %}
      {% for article in articles %}
          <p>{{ article.pk }}</p>
      {% endfor %}
  {% endblock %}
  ```

<br>

#### base.html 목록 바로 가기 추가

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Instagram</title>
      {% block css %}
      {% endblock %}
  </head>
  <body>
      {% block body %}
      {% endblock %}
      <a href="{% url 'articles:index' %}" >목록 </a>
  </body>
  </html>
  ```

<br>

#### 루트 페이지 설정

> 프로젝트폴더/ urls.py

- ```python
  from django.contrib import admin
  from django.urls import path, include
  
  from articles import views
  urlpatterns = [
      path('', views.index),
  	path('admin/', admin.site.urls),
  	path('articles/', include('articles.urls')),
  ]
  ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m "Add Index page"
  ```

<br>

#### create 로직 만들기

##### urls.py

- ```python
  from django.urls import path 
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
  	path('', views.index, name='index'),
      path('create/', views.create, name='create'),
  ]
  ```

  

##### views.py

- modelForm 가져오기

- ```python
  from .forms import ArticleForm
  ```

- ```python
  from .forms import ArticleForm
  
  def create(reqeust):
      form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/forms.html', context)
  ```

  

##### forms.html

- form 구조 만들어주기

- ```html
  {% extends 'base.html'%}
  
  {% block title %}새 글쓰기 {% endblock %}
  {% block body %}
  	<form action="" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>작성</button>
  	</form>
  ```

  - POST로 요청 시, `{% csrf_token %} 꼭 작성해주기 



##### views.py

- 글을 쓰면 써지게끔 만들어야 하므로 분기작업을 한다.

  - 사용자의 값을 받고, 검증을 받고, 저장하거나 다시 Form으로 보낸다.

- ```python
  from django.shortcuts import render, redirect 
  
  from .forms import ArticleForm
  
  def create(reqeust):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:index')
      else:
          form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/forms.html', context)
  ```

<br>

#### 메시지 (New learning material!)

##### 사용자들에게 **<u>form 양식에 왜 맞지 않는지 친절하게 알려주기</u>** 위한 방법 :) 

- <a href="https://docs.djangoproject.com/en/3.0/ref/contrib/messages/">Django Messages Framework</a>

  - one-time notification message also known as flash message (1번만 알림으로 메시지 보내는 기능)

  - DJango provides full support for cookie-and session-based messaging

  - temporarily store messages in one request: 한 번의 요청에 임시적으로 메시지를 저장한다.

  - Enabling messages: django-admin startproject already contains all the settings requred to enable message functionality

    1. `django.contrib.messages'` is in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-INSTALLED_APPS).

    2. [`MIDDLEWARE`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MIDDLEWARE) contains `'django.contrib.sessions.middleware.SessionMiddleware'` and `'django.contrib.messages.middleware.MessageMiddleware'`.

       The default [storage backend](https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#message-storage-backends) relies on [sessions](https://docs.djangoproject.com/en/3.0/topics/http/sessions/). That’s why `SessionMiddleware` must be enabled and appear before `MessageMiddleware` in [`MIDDLEWARE`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MIDDLEWARE).

    3. The `'context_processors'` option of the `DjangoTemplates` backend defined in your [`TEMPLATES`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-TEMPLATES) setting contains `'django.contrib.messages.context_processors.messages'`.

  - Using messages in views and templates의 내용을 따라해보자

##### Adding a message

- ```python
  from django.contrib import messages
  messages.add_message(request, messages.INFO, 'Hello world.')
  ```

- ```python
  messages.debug(request, '%s SQL statements were executed.' % count)
  messages.info(request, 'Three credits remain in your account.')
  messages.success(request, 'Profile details updated.')
  messages.warning(request, 'Your account expires in three days.')
  messages.error(request, 'Document deleted.')
  ```

  - bootstrap에서 많이 봤던 코드인데 보통 debug level에서 많이 쓰이는 표현이다.

##### views.py

- ```python
  from django.contrib import messages
  from django.shortcuts import render, redirect 
  
  from .forms import ArticleForm
  
  def create(reqeust):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:index')
           messages.warning(request, '폼을 다시 확인 후 제출해주세요.')
      else:
          form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/forms.html', context)
  ```

<br>

##### 메시지를 언제 보여줄까? (Display messages)

> 아래 메시지 추가해주기

- ```python
  {% if messages %}
  <ul class="messages">
      {% for message in messages %}
      <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
      {% endfor %}
  </ul>
  {% endif %}
  ```

  

###### base.html

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Instagram</title>
      {% block css %}
      {% endblock %}
  </head>
  <body>
      {% if messages %}
      <ul class="messages">
          {% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
          {% endfor %}
      </ul>
      {% endif %}
      {% block body %}
      {% endblock %}
      <a href="{% url 'articles:index' %}" >목록 </a>
  </body>
  </html>
  ```

<br>

##### warning message 부트스트랩으로 꾸미기

###### warning파트를 Bootstrap에서 그대로 가져온다.

- <a href="https://getbootstrap.com/docs/4.0/components/alerts/">Bootstrap Alerts </a>

- ```html
  <div class="alert alert-primary" role="alert">
    This is a primary alert—check it out!
  </div>
  ```

###### Bootstrap CDN 넣기

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Instagram</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
      {% block css %}
      {% endblock %}
  </head>
  <body>
      {% if messages %}
      <ul class="messages">
          {% for message in messages %}
          <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
          {% endfor %}
      </ul>
      {% endif %}
      {% block body %}
      {% endblock %}
      <a href="{% url 'articles:index' %}" >목록 </a>
      <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  



###### base.html

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Instagram</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
      {% block css %}
      {% endblock %}
  </head>
  <body>
      {% if messages %}
      <div class="messages">
          {% for message in messages %}
          <div class="alert alert-{% if message.tags %}{{ message.tags }}{% endif %}" role="alert"> 
              {{message}}
          </div>
          {% endfor %}
      </div>
      {% endif %}
      {% block body %}
      {% endblock %}
      <a href="{% url 'articles:index' %}" >목록 </a>
      <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  

##### 'TEMPLATES' - 'OPTIONS' - 'context_proecessors'

- `context_processors`: html 템플릿에서 어떠한 변수들을 기본적으로 쓸 수 있는지 설정
  - message, request
- 내부에 있는 `django.contrib.messages.context_processors.message` 때문에 메시지 사용 가능

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m "Add create page with message frameworks"
  ```

<br>

#### Detail 페이지 생성

##### urls.py

> variable routing 구성이 필수다!

- ```python
  from django.urls import path 
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
  	path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>/', views.detail, name='detail'),
  ]
  ```

  

##### views.py

- ```python
  from django.shortcuts import render, redirect, get_object_or_404
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article
      }
      return render(request, 'articles/detail.html', context)
  ```

  - `get_object_or_404`
    - object 를 가져오거나, 없으면 404 에러페이지 띄어주기
  - Python 함수와 변수는:  snake_case 사용
  - 클래스: CamelCase 사용



##### detail.html

- ```html
  {% extends 'base.html' %}
  
  {% block title %} {{article.pk}}글 {% endblock %}
  
  {% block body %}
  <h2> {{article.pk}} : {{ article.title}} </h2>
  <p> {{ article.content }}</p>
  {% endblock %}
  ```



##### index.html (글 보러가기 링크 생성)

- ```html
  {% extends 'base.html' %}
  
  {% block title %}목록 {% endblock %}
  
  {% block body %}
      {% for article in articles %}
          <p>{{ article.pk }}</p>
  		<a href="{% url 'articles:detail' article.pk %}">글 보러가기 </a>
      {% endfor %}
  {% endblock %}
  ```

  - 글 보러가기 링크 생성



##### urls.py

- redirect url 변경 (detail 페이지로 가게끔) #부분 참고

  - ```python
    from django.contrib import messages
    from django.shortcuts import render, redirect 
    
    from .forms import ArticleForm
    
    def create(reqeust):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk) ####
             messages.warning(request, '폼을 다시 확인 후 제출해주세요.')
        else:
            form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'articles/forms.html', context)
    ```

<br>

#### git commit

- ```bash
  $ git add .
  $ git commit -m 'Add detail page'
  ```

<br>

## 오후 2시 zoom

- new
  - 글 작성 페이지 (form)
- create
  - DB에 저장
  - render('create.html', {'success':True})
  - redirect(성공여부)
  - redirect('articles:index')
- Message
  - 이전의 상태를 다음  Request & respond

<br>

### HTTP

> 요청과 응답의 반복이다.
>
> 요청을 보내고, 서버는 해당하는 응답을 보내준다

- `stateless(무상태성)`: 상태가 없다는 말은, 과거를 모른다는 말
  - 이전에 했던 것들을 기반으로 하는 것이 아니라, 완전히 base인 상태에서 요청을 이루는 것
- `connectionless(무연결성)`

<br>

### Article CRUD

- title, content, created_at, updated_at

<br>

### User CRUD

- username, password
- 직접 < Django

- `app_name = 'users'`

  - ```python
    class User(models.Model):
        username = CharField
        password = CharField
        created_at
        updated_at
    ```

- 기존: new/create/detail/index/edit/update/delete
- 새로 묶은 방법: create/detail/index/update/delete

<br>

## 오후 라이브 강의

- 장고 내부에는 **<u>user class 와 user를 생성</u>**할 수 있는 **model form**이 만들어져있다.

<br>

### Message Storage

- django에서 기본적으로 message framework를 구동하는 방식은 Fallback Storage.

  - 먼저 cookie를 적용되고, 그렇지 않으면 session을 사용.

- 로컬 환경에서는 기본적으로 session을 사용한다.
  - settings.py

  - ```
    MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorate '
    ```

<br>

### 회원가입

> Django는 회원가입을 구성할 때 편하게 구성할 수 있다.

- 핵심:star: : **Django 내부에 있는 User 클래스, ModelForm 활용** 

<br>

#### 앱 생성

- django_form 프로젝트 폴더

- 새로운 계정들을 관리하기 위해 앱 생성

  - ```bash
    $ python manage.py startapp accounts
    ```

<br>

#### 앱 등록

- settings.py

  - ```python
    INSTALLED_APPS = [
        'accounts',
    ]
    ```

<br>

#### 아래와 같이 하면 안된다!!

##### 모델 정의

- 회원가입할 때 어떠한 것들을 받으면 좋을까? username, password

- models.py

  - ```python
    class Account(models.Model):
    	username = models.CharField(max_length=16)
        password= models.CharField(max_length=16)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_add=True)
    ```

    - 프로필이 수정될 수도 있으니 updated_at도 추가한다.

<br>

##### urls.py

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
  ]
  ```
  - 회원가입 페이지를 구현하기 위해, signup url을 만들어준다.
  - app_name 역시 만들어준다.'

<br>

##### migrate 파일 만들기, 반영하기

 -  ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

<br>

##### forms.py

- `forms.py` 파일 생성

  - ```python
    from django import forms
    from .models import Account
    
    class AccountForm(forms.ModelForm):
        class Meta:
            model = Account
            fields = '__all__'
    ```
  

<br>

##### views.py

- views.py

  - ```python
    from django.shortcuts import render
    from .forms import AccountForm
    def signup(request):
        form = AccountForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)
    ```

- signup.html

  - ```python
    {{ form.as_p }}
    ```

- projectfolder/urls.py

  - ```python
  urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
        path('accounts/', include('accounts.urls')),
    ]
    ```



##### ⚠️문제점

![capture-7278826](images/20200413_TIL/capture-7278826.png)

- 위와 같이 만들면: Password confirmation도 없을 뿐더러
- 사용자가 비밀번호를 1q2w3e4r과 같은 패스워드를 저장하면, 비밀번호가 그대로 노출된다.
- **<u>회원가입을 할 때에는 항상 DB의 모든 비밀번호가 보이면 안된다</u>**.
- 일반적으로 회원가입을 구성할 때에는 User에 대한 DataBase를 저장하는 것이다.
  - User DataBase에서 **가장 중요한 파트는 password**이다.
  - **암호화를 해서 저장**해야 보안에 대해서 책임을 질 수 있다.



##### DB & Migration 파일 지우기

- 파일들 삭제
- Models.py도 삭제!!!
- forms.py도 삭제!!
- Views.py도 삭제!!
- url 설정도 지우자..





#### 회원가입 할 시에는 아래 방식을 따라야 한다.

##### User Model 자체를 생각하자.

- settings.py의 INSTALLED_APPS에 'django_extensions' 추가

##### shell plus

- **django내부에 있는 model과 우리가 등록한 model이 자동으로 import 된다**.
- 유저 모델도 이미 import되어 있다. `from django.contrib.auth.model import Group, Permission, User `
  - 실제 회원가입 기능이 내부적으로 있었다.
    - 예시: `python manage.py createsuperuser`
- django에서는 내부에 있는 유저 모델을 사용하면 된다



##### app/urls.py

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
  ]
  ```



##### views.py

###### `from django.contrib.auth.forms import UserCreationForm`

- Django에는 유저 생성 폼이 있다.

- ```python
  from django.shortcuts import render
  from django.contrib.auth.forms import UserCreationForm
  
  def signup(request):
      form = UserCreationForm
      context = {
          'form': form
      }
      return render(request, 'accounts/signup.html', context)
  ```

- 서버를 실행시키면 아래와 같은 페이지가 나타난다.

  ![capture-7279383](images/20200413_TIL/capture-7279383.png)

  - 이미 사용자 이름과 비밀번호, 비밀번호 확인이 구현되어 있다.

##### signup.html

- ```html
  {% extends 'base.html' %}
  
  {% block body %}
  	<form action="" method="POST">
  		{% csrf_token %}
          {{ form.as_p }}
          <button>회원가입</button>
  	</form>
  {% endblock %}
  ```



##### 내용 입력 후 신청을 하면 회원을 등록할 수 있도록 분기한다.

###### views.py

- ```python
  from django.shortcuts import render, redirect
  from django.contrib.auth.forms import UserCreationForm
  
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              #게시글 목록 페이지로 보내준다
              return redirect('articles:index')
      form = UserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/signup.html', context)
  ```



### django Github

> <a href="https://github.com/django/django">Django Github </a>

#### django-contrib-auth- forms.py

##### UserCreationForm(Forms.ModelForm)

- ```python
  class UserCreationForm(forms.ModelForm):
      """
      A form that creates a user, with no privileges, from the given username and
      password.
      """
      error_messages = {
          'password_mismatch': _('The two password fields didn’t match.'),
      }
      password1 = forms.CharField(
          label=_("Password"),
          strip=False,
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
          help_text=password_validation.password_validators_help_text_html(),
      )
      password2 = forms.CharField(
          label=_("Password confirmation"),
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
          strip=False,
          help_text=_("Enter the same password as before, for verification."),
      )
  
      class Meta:
          model = User
          fields = ("username",)
          field_classes = {'username': UsernameField}
  
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          if self._meta.model.USERNAME_FIELD in self.fields:
              self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True
  
      def clean_password2(self):
          password1 = self.cleaned_data.get("password1")
          password2 = self.cleaned_data.get("password2")
          if password1 and password2 and password1 != password2:
              raise forms.ValidationError(
                  self.error_messages['password_mismatch'],
                  code='password_mismatch',
              )
          return password2
  
      def _post_clean(self):
          super()._post_clean()
          # Validate the password after self.instance is updated with form data
          # by super().
          password = self.cleaned_data.get('password2')
          if password:
              try:
                  password_validation.validate_password(password, self.instance)
              except forms.ValidationError as error:
                  self.add_error('password2', error)
  
      def save(self, commit=True):
          user = super().save(commit=False)
          user.set_password(self.cleaned_data["password1"])
          if commit:
              user.save()
          return user
  ```

  1. ModelForm을 상속받고 있다.
  2. 패스워드는 password1, password2로 해서 CharField를 만들어놓고, label로 Password, Password Confirmation으로 2가지를 구성해놓았다.
     - **실제 DB에는 username과 password를 저장하는데, 우리가 input으로 받을 때에는, password 1, 2를 만들어서 이 두 가지가 맞는지 검증을 해야하기 때문에 2개의 password field를 만들었다.**
  3. ModelForm에는 항상 Meta가 필요!
     - `model`은 User이며
     - `fields`는 username
  4. `def clean_password2`
     - users는 저장할 때의 과정:
       - password 1과 2가 맞는지 비교하고,
       - 검증하고,
       - 저장한다.

  5. `def save`
     - save 후 password를 내부적으로 클린한 패스워드를 바탕으로 set한다.

#### User모델은 어떻게 정의되어 있을까?

##### django-contrib-auth-models.py

##### class User(AbstractUser)

- ```python
  class User(AbstractUser):
      """
      Users within the Django authentication system are represented by this
      model.
      Username and password are required. Other fields are optional.
      """
      class Meta(AbstractUser.Meta):
          swappable = 'AUTH_USER_MODEL'
  
  ```
  - AbstractUser를 상속받고 있다.

##### class AbstractUser

- ```python
  class AbstractUser(AbstractBaseUser, PermissionsMixin):
      """
      An abstract base class implementing a fully featured User model with
      admin-compliant permissions.
      Username and password are required. Other fields are optional.
      """
      username_validator = UnicodeUsernameValidator()
  
      username = models.CharField(
          _('username'),
          max_length=150,
          unique=True,
          help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
          validators=[username_validator],
          error_messages={
              'unique': _("A user with that username already exists."),
          },
      )
      first_name = models.CharField(_('first name'), max_length=150, blank=True)
      last_name = models.CharField(_('last name'), max_length=150, blank=True)
      email = models.EmailField(_('email address'), blank=True)
      is_staff = models.BooleanField(
          _('staff status'),
          default=False,
          help_text=_('Designates whether the user can log into this admin site.'),
      )
      is_active = models.BooleanField(
          _('active'),
          default=True,
          help_text=_(
              'Designates whether this user should be treated as active. '
              'Unselect this instead of deleting accounts.'
          ),
      )
      date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  
      objects = UserManager()
  
      EMAIL_FIELD = 'email'
      USERNAME_FIELD = 'username'
      REQUIRED_FIELDS = ['email']
  
      class Meta:
          verbose_name = _('user')
          verbose_name_plural = _('users')
          abstract = True
  
      def clean(self):
          super().clean()
          self.email = self.__class__.objects.normalize_email(self.email)
  
      def get_full_name(self):
          """
          Return the first_name plus the last_name, with a space in between.
          """
          full_name = '%s %s' % (self.first_name, self.last_name)
          return full_name.strip()
  
      def get_short_name(self):
          """Return the short name for the user."""
          return self.first_name
  
      def email_user(self, subject, message, from_email=None, **kwargs):
          """Send an email to this user."""
          send_mail(subject, message, from_email, [self.email], **kwargs)
  
  ```

  - username, first name, lastname등 다양한 정보를 담고 있다.



### User objects

> <a href="https://docs.djangoproject.com/en/3.0/topics/auth/default/#user-objects">Django Documentation User Objects</a>

#### User의 디폴트 속성 

- username
- password
- email
- first_name
- last_name



#### User를 만드는 과정

> Creating Users

- `create_user()` 메소드를 사용하라!
  - 비밀번호 암호화 때문에 이 메소드를 사용
  - 패스워드 파트가 고려가 된 메소드이다.

- ```python
  >>> from django.contrib.auth.models import User
  >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  
  # At this point, user is a User object that has already been saved
  # to the database. You can continue to change its attributes
  # if you want to change other fields.
  >>> user.last_name = 'Lennon'
  >>> user.save()
  ```

  

- app/urls.py

  - ```python
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('articles/', views.articles, name='article')
    ]
    ```

- 회원가입을 구성하게 되면: user의 DB를 갖게 된다

  - password는 암호화해서 보안을 지켜야한다.



### shell plus

- ```python
  u = User.objects.create(username='John', password='1q2w3e4r')
  
  u
  >> <User: John>
      
  User.objects.all()
  >> <QuerySEt [<User: admin>, <User: hong>, <User: John>]
  
  u.password
  >> '1q2w3e4r'
  
  admin = User.objects.get(pk=1)
  
  admin.password
  >> 'pbkdf2_sha256$120000$CfaLeR06pw9G$ff10raKvQ9FN0tXGtjABQoAy3osmx2dAv63ywkZU7Dg='
  
  real = User.objects.create_user(username='realjohn', password='1q2w3e4r')
  
  real.password
  >> 'pbkdf2_sha256$120000$bIx5CLfAq3fY$hySpT3rXIqqN70ykFmZiAvn7WiaYnxhzNbO..'
  ```

  - User.objects.create로 그냥 username과 password를 만들면 `1q2w3e4r` 처럼 그냥 보인다.
  - 하지만 6번처럼 create.user라는 메소드를 쓰게 되면 admin 패스워드가 복잡한 형식으로 알아볼 수 없는 형식으로 변환됐다.
  - 즉, 비밀번호가 암호화되어 구성이 되어있다.



### 패스워드 알고리즘 방식 (비밀번호 암호화)

> <a href="https://d2.naver.com/helloworld/318732">네이버 참고</a>

- 비밀번호 검증은 ModelForm이 검증을 한다.

![capture-7281438](images/20200413_TIL/capture-7281438.png)

- admin은 알고리즘 반복, 솔트, 해시 등으로 구성되어있다.

![capture-7281477](images/20200413_TIL/capture-7281477.png)

- 일반 사용자 주소로 들어가면 비밀번호 란에 '잘못된 비밀번호 형식이거나 알 수 없는 해싱 알고리즘입니다'라고 뜬다.

#### 해시함수

- 일반적으로 비밀번호는 DB에 그대로 저장하지 못한다.
- 사람들은 못알아보는 형식으로 문자열을 바꿔서 DB에 저장해야 한다.
- 이 때 활용하는 것이 **<u>해시함수</u>**!!!

#### SHA256

- 대표적인 해시 함수
- **단방향 알고리즘**: 암호화된 비밀번호으로 변환할 수 있지만, 이 암호화된 비밀번호를 가지고 있어도 **역으로 원래의 비밀번호가 어떠한 문자열로 만들어졌는지 알 수 없다**.  (역으로 연산을 할 수 없다.)
- `SHA`: Secure Hash Algorithm
- 블록체인에서 많이 사용한다.

#### import hashlib

- ```python 
  python
  
  import hashlib
  
  pw = '1q2w3e4r'
  
  h = hashlib.sha256(pw.encode())
  
  h
  >> <sha256 HASH object @0x7fc3bab97360>
  
  h.hexdigest()
  >> '72ab994fa2eb426c051ef59cad617750bfe06d7cf6311285ff79c19c32afd236'
  ```

  - python 내부에도 간단하게 이미 내장 라이브러리로 구성되어있다.
  - digest값을 추출해서 볼 수 있다.
  - **문자열이 동일하면 값은 동일하다.** 그러나 한 글자라도 바뀌면, 이 값은 변환된다.

#### rainbow 공격

-  DB를 털었는데 똑같은 값이 너무 많다!
- 그러면 그 똑같은 값이 실제 무슨 값인지 뭔지 찾으면 된다.
- 이를 대비하기 위한 것이 Salt

#### Salt

- 그렇기 때문에 모두가 같은 값을 적더라도 DB에는 다른 값을 적게 하고 싶다. 이 것이 **<u>SALT</u>**!!

#### 반복

-  Brute Force로 탐색해서 찾을 수 있지만, 1개를 검증하는데 기존에 1초 걸리는걸 반복을 120000으로 하면 120000초로 해서, 검증 시간을 늘려버린다.

#### pdfdf2

- 가장 많이 사용되는 key derivation function은 PBKDF2이다.
- 해시 함수의 컨테이너인 PBKDF2는 솔트를 적용한 후, 해시 함수의 반복 횟수를 임의로 선택할 수 있다.
- PBKDF2는 아주 가볍고 구현하기 쉬우며, SHA와 같이 검증된 해시 함수만을 사용한다.

#### md5

- 이미 복호화되어 있다.



### 패스워드 변경 (`set_password`)

- 패스워드 변경할 때는 `set_password`라는 함수를 통해 패스워드를 변경해야 한다.

- ```python
  >>> from django.contrib.auth.models import User
  >>> u = User.objects.get(username='john')
  >>> u.set_password('new password')
  >>> u.save()
  ```





### User detail 페이지 만들기

#### urls.py

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
      path('<int:pk>/', views.detail, name='detail'),
  ]
  
  ```



#### views.py

- ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserCreationForm
  # from django.contrib.auth.models import User
  
  # Create your views here.
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              # 게시글 목록 페이지
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form
      }
      return render(request, 'accounts/signup.html', context)
  
  def detail(request, pk):
      User = get_user_model()
      user = get_object_or_404(User, pk=pk)
      context = {
          'user': user
      }
      return render(request, 'accounts/detail.html', context)
  
  ```

  - **user를 가지고 오기 위해서는 `from django.contrib.auth import get_user_model`**
    - from django.contrib.auth.models import User 대신  `from django.contrib.auth import get_user_model`사용
    - 유저를 커스텀할 때 유용

  

#### detail.html

- 파일 생성

- ```html
  {% extends 'base.html' %}
  
  {% block body %}
  <h1>{{ user.pk }} : {{ user.username }}</h1>
  <hr>
  {% endblock %}
  ```

  - 각 user의 페이지를 볼 수 있다.



### Update마저도 내부에 있는 form을 사용할 수 있다.

#### urls.py

- ```python
  from django.urls import path
  from . import views
  
  app_name = 'accounts'
  urlpatterns = [
      path('signup/', views.signup, name='signup'),
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```



#### views.py

> `from django.contrib.auto.forms import UserCreationForm, UserChangeForm`
>
> UserChangeForm을 활용한다!

- ```python
  def update(request, pk):
  	form = UserChangeForm()
      context = {
          'form':form
      }
      return render(request, 'accounts/update.html', context)
  ```

  

#### update.html

- ```python
  {% extends 'base.html' %}
  
  {% block body %}
  	<form action="" method="POST">
  		{% csrf_token %}
          {{ form.as_p }}
          <button>회원정보 수정</button>
  	</form>
  {% endblock %}
  ```

- ![capture 11](images/20200413_TIL/capture 11.png)

  - 기본적으로 저장되어 있는 값들이 너무 많다.
  - 마지막 로그인 시간, 스태프 권환, 활성, 이메일, 이름, 성, 사용자 이름 등 모두 다 기록되게끔 고려가 되어있다.
  - 그러다 보니 User Class를 그대로 가져다 쓴다.
  - **사용자 이름, 이름, 성, 이메일 주소만 보여주고 싶고, 마지막 로그인, 그룹, 사용자 권한 등은 내부적으로 관리하고 싶을 때는?**
    - **<u>이 form을 상속받아서 내가 원하는 값들을 설정한다</u>**.
      - metafield 관리, override 사용



#### forms.py

- ```python
  from django.contrib.auth import get_user_model #model을 가져온다
  from django.contrib.auth.forms import UserChangeForm
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields=['username', 'first_name', 'last_name', 'email']
  ```

  

#### views.py

- ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserCreationForm
  from .forms import CustomUserChangeForm
  
  def update(request, pk):
      form = CustomUserChangeForm()
      context= {
          'form': form
      }
      return render(request, 'accounts/update.html', context)
  ```

- ![capture-7283755](images/20200413_TIL/capture-7283755.png)



### 정리

- django 내부에는 user라는 클래스가 있다.
  - Users는 AbstractUser 클래스를 상속받고 있다. (username, email, firstname, lastname...)
- 이를 커스터마이징 하고 싶다면?
  - CustomerUser이라는 나만의 UserClass를 만들면 된다!!
  - **상속을 통해서 활용하면 된다.**
- **상속을 받아서 몇개의 fields를 받는 등 직접 정의를 한다.**



<br>

##  오후 4시 zoom

`Article.objects.all()` -> Disk Drive

- 매우 헤비한 쿼리문
- 데이터를 다 들고와라

<br>

### 회원가입 (신규 User → DB)

- UserCreationForm(C)

  → `User.objects.create_users(DB 검증)`

- UserChangeForm(U)

<br>

### 로그인  (기존 User → DB에 있는지 검증)

- 12341234 + 소금 + iteration

  - ```python
    for _ in range(360000):
    	hashlib.sha256('1q2w3e4r')
    ```

- 1a2s3e4r5t

- 72ab

- Sha

  - git에 쓰인다.
  - 16진수: git commit hash
  - transitioning Git to SHA-256



<br>

## 퀴즈

- ModelForm은 class Meta를 통해 model 정보만 설정하면 된다. : X
- DB에 해당 오브젝트가 없는 경우 404 status code를 반환하려고 한다. 이를 위해 django.shortcuts에 정의되어 있는 함수의 이름은? :get_object_or_404
- Django 회원가입 구현시 활용 가능한 django 내부에 작성되어 있는 Form은 ModelForm을 기반으로 작성되었다.: O
- Django 회원가입 구현시 활용 가능한 django 내부에 작성되어 있는 Form은 UserSignUpForm이다.: X