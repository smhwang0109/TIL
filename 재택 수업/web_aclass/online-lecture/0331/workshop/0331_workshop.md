# 0331_workshop

![캡처1](C:\Users\user\house\web_aclass\online-lecture\0331\workshop\캡처1.PNG)

![캡처2](C:\Users\user\house\web_aclass\online-lecture\0331\workshop\캡처2.PNG)

![캡처3](C:\Users\user\house\web_aclass\online-lecture\0331\workshop\캡처3.PNG)

1. crud/settings.py

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   

2. crud/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls'))
   ]
   ```

   

3. articles/urls.py

   ```python
   from django.urls import path
   
   from . import views
   
   urlpatterns = [
       path('new/', views.new),
       path('', views.index),
       path('create/', views.create),
   ]
   ```

   

4. articles/views.py

   ```python
   from django.shortcuts import render
   
   from .models import Article
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       title = request.GET.get('title')
       content = request.GET.get('content')
       article = Article()
       article.title = title
       article.content = content
       article.save()
       return render(request, 'articles/create.html')
   
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles':articles
       }
       return render(request, 'articles/index.html', context)
   ```

   

5. crud/templates/base.html

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>0331-exercise</title>
   </head>
   <body>
       <hr>
       <h1>Articles</h1>
       <hr>
       {% block content %}
       {% endblock %}
   </body>
   </html>
   ```

   

6. templates/articles/index.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <a href="/articles/new/">NEW</a>
   <h2>게시글 모음</h2>
   <ul>
       {% for article in articles %}
           <li>
               <h3>제목: {{ article.title }}</h3>
               <p>내용: {{ article.content }}</p>
           </li>
       {% endfor %}
   </ul>
   {% endblock %}
   ```

   

7. templates/articles/new.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h2>글 작성</h2>
   <br>
   <form action="/articles/create/">
       제목: <input type="text" name="title"><br>
       내용: <input type="text" name="content"><br>
       <input type="submit" value="게시글 작성">
   </form>
   <hr>
   <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   

8. templates/articles/create.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h2>성공적으로 글이 작성되었습니다.</h2>
   <hr>
   <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   