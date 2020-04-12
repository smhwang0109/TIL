# 0331_exercise

![캡처1](C:\Users\user\house\web_aclass\online-lecture\0331\exercise\캡처1.PNG)

![캡처2](C:\Users\user\house\web_aclass\online-lecture\0331\exercise\캡처2.PNG)

1. articles/views.py

   ```python
   from django.shortcuts import render
   
   # Create your views here.
   def ping(request):
       return render(request, 'articles/ping.html')
   
   def pong(request):
       ping = request.GET.get('ping')
       context = {
           'ping' : ping
       }
       return render(request, 'articles/pong.html', context)
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
       path('ping/', views.ping),
       path('pong/', views.pong),
   ]
   ```

   

4. base.html

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
       {% block content %}
       {% endblock %}
   </body>
   </html>
   ```

   

5. ping.html

   ```html
   {% extends 'base.html' %}
   {% block content %}
   <h1>여기는 ping</h1>
   <h2>pong으로 데이터를 보내보자</h2>
   <form action="/articles/pong/">
       <input type="text" name="ping">
       <button typer="submit">submit</button>
   </form>
   {% endblock %}
   ```

   

6. pong.html

   ```html
   {% extends 'base.html' %}
   {% block content %}
   <h1>여기는 pong</h1>
   <h2>ping에서 {{ ping }}를 받았어!</h2>
   {% endblock %}
   ```

   

