# 0326_workshop

![캡처](C:\Users\user\house\web_aclass\online-lecture\0326\workshop\캡처.PNG)

1. intro/urls.py

   ```python
   from django.contrib import admin
   from django.urls import path
   from pages import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('lotto/', views.lotto),
   ]
   ```

   

2. pages/views.py

   ```python
   from django.shortcuts import render
   
   def lotto(request):
       import random
       number_list = sorted(random.sample(range(1,46), 6))
       result = {'numbers' : number_list}
       return render(request, 'lotto.html', result)
   ```

   

3. templates/lotto.html

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Lotto</title>
   </head>
   <body>
       <h1>제 325회 로또 번호 추천</h1>
       <p>SSAFY님께서 선택하신 로또 번호는 {{ numbers }}입니다.</p>
   </body>
   </html>
   ```

   