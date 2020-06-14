# 0327_workshop

![캡처](C:\Users\user\house\web_aclass\online-lecture\0327\workshop\캡처.PNG)

![캡처2](C:\Users\user\house\web_aclass\online-lecture\0327\workshop\캡처2.PNG)

1. intro/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('dinner/<str:menu>/<int:people>', views.dinner),
   ]
   ```

   

2. pages/views.py

   ```python
   from django.shortcuts import render
   
   def dinner(request, menu, people):
       context = {
           'menu':menu,
           'people':people,
       }
       return render(request, 'dinner.html', context)
   ```

   

3. templates/dinner.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>저녁 메뉴</h1>
       <h1>저녁 먹을 사람?! {{ people }}명</h1>
       <h1>어떤 메뉴?! {{ menu }}</h1>
   </body>
   </html>
   ```

   