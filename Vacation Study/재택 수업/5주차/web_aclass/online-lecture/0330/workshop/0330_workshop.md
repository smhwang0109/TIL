# 0330_workshop

![캡처1](C:\Users\user\house\web_aclass\online-lecture\0330\workshop\캡처1.PNG)

![캡처2](C:\Users\user\house\web_aclass\online-lecture\0330\workshop\캡처2.PNG)

![캡처3](C:\Users\user\house\web_aclass\online-lecture\0330\workshop\캡처3.PNG)

1. mygallery/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path
   
   from pages import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('pages/', views.index),
       path('pages/gallery/', views.gallery),
   ]
   ```

   

2. pages/views.py (YOUR_ACCESS_KEY 대체)

   ```python
   from django.shortcuts import render
   import requests
   
   def index(request):
       return render(request, 'index.html')
   
   def gallery(request):
       category = request.GET.get('category')
       url = 'https://api.unsplash.com/search/photos?client_id=YOUR_ACCESS_KEY&query={}'.format(category)
       D = requests.get(url).json()
       context = {
           'img_url':D['results']
       }
       return render(request, 'gallery.html', context)
   ```

   

3. templates/index.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>pages-index</title>
   </head>
   <body>
       <h1>고화질 이미지 생성기</h1>
       <h2>원하는 카테고리를 입력하세요!</h2>
       <form action="/pages/gallery/">
           <input type="text" name="category">
           <button type="submit">Submit</button>
       </form>
   </body>
   </html>
   ```

   

4. templates/gallery.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>pages-gallery</title>
   </head>
   <body>
       {% if img_url %}
       {% for result in img_url %}
       <img src="{{ result.urls.regular }}">
       {% endfor %}
       {% else %}
       <h1>해당 카테고리에 해당하는 이미지가 없습니다.</h1>
       {% endif %}
   </body>
   </html>
   ```

   
