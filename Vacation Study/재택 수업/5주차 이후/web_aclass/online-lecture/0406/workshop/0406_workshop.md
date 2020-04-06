# 0406_workshop

![캡처1](C:\Users\user\house\web_aclass\online-lecture\0406\workshop\캡처1.PNG)

![캡처2](C:\Users\user\house\web_aclass\online-lecture\0406\workshop\캡처2.PNG)

![캡처3](C:\Users\user\house\web_aclass\online-lecture\0406\workshop\캡처3.PNG)

![캡처4](C:\Users\user\house\web_aclass\online-lecture\0406\workshop\캡처4.PNG)

1. crud/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('articles/', include('articles.urls')),
   
       path('admin/', admin.site.urls),
   ]
   ```

   

2. articles/urls.py

   ```python
   from django.urls import path
   from . import views
   
   app_name='articles'
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('<int:pk>/', views.detail, name='detail'),
       path('<int:pk>/edit/', views.update, name='edit'),
       path('create/', views.create, name='create'),
       path('<int:pk>/delete/', views.delete, name='delete'),
   ]
   ```

   

3. articles/models.py

   ```python
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=126)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return f'{self.title}: {self.content}'
   ```

   

4. articles/views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from .models import Article
   
   def index(request):
       articles = Article.objects.all()
       context = {
           'articles': articles
       }
       return render(request, 'articles/index.html', context)
   
   def detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       context = {
           'article':article
       }
       return render(request, 'articles/detail.html', context)
   
   def new(request):
       return render(request, 'articles/upload.html')
   
   def update(request, pk):
       article = get_object_or_404(Article, pk=pk)
       context = {
           'article':article
       }
       return render(request, 'articles/upload.html', context)
   
   def create(request):
       pk = request.POST.get('check')
       if pk:
           article = get_object_or_404(Article, pk=pk)
       else:
           article = Article()
       article.title = request.POST.get('title')
       article.content = request.POST.get('content')
       article.save()
       return redirect('articles:detail', article.pk)
   
   def delete(request, pk):
       article = get_object_or_404(Article, pk=pk)
       article.delete()
       return redirect('articles:index')
   ```

   

5. templates/base.html

   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <!-- Required meta tags -->
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   
       <!-- Bootstrap CSS -->
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
   
       <title>crud</title>
     </head>
     <body>
       <div class="m-5">
         {% block content %}
         {% endblock %}
       </div>
   
   
       <!-- Optional JavaScript -->
       <!-- jQuery first, then Popper.js, then Bootstrap JS -->
       <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
     </body>
   </html>
   ```

   

6. articels/templates/articles/index.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>INDEX</h1>
   <a href="{% url 'articles:new' %}">NEW</a>
   <br>
   {% for article in articles %}
   <h2>제목: {{ article.title }}</h2>
   <p>내용: {{ article.content }}</p>
   <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
   <hr>
   {% endfor %}
   {% endblock %}
   ```

   

7. articels/templates/articles/detail.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>DETAIL</h1>
   <hr>
   <h2>{{article.title}}</h2>
   <p>{{article.content}}</p>
   <p>작성일: {{article.created_at}}</p>
   <p>수정일: {{article.updated_at}}</p>
   <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
   <a href="{% url 'articles:delete' article.pk %}">DELETE</a><br>
   <a href="{% url 'articles:index' %}">BACK</a>
   
   
   {% endblock %}
   ```

   

8. articels/templates/articles/upload.html

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   {% if article %}
   <h1>EDIT</h1>
   {% else %}
   <h1>NEW</h1>
   {% endif %}
   <form action="{% url 'articles:create' %}" method="POST">
       {% csrf_token %}
       <label for="title">TITLE:</label>
       <input type="text" {% if article %} value="{{article.title}}" {% endif %} id="title" name="title"><br>
       <label for="content">CONTENT:</label>
       <textarea name="content" id="content" rows="10">{% if article %} {{article.content}} {% endif %}</textarea><br>
       {% if article %}
       <input type="hidden" name="check" value="{{article.pk}}">
       <input type="submit" value="수정">
       {% else %}
       <input type="hidden" name="check" value="">
       <input type="submit" value="작성">
       {% endif %}
   </form>
   {% if article %}
   <a href="{% url 'articles:detail' article.pk %}">BACK</a>
   {% else %}
   <a href="{% url 'articles:index' %}">BACK</a>
   {% endif %}
   {% endblock %}
   ```