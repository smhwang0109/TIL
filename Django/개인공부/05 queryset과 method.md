# 05 queryset과 method

## queryset

클래스에서 objects 메소드를 사용하여 모델의 객체 불러옴

이 때 전달받은 객체가 queryset

```python
# views.py
from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})
```

blogs 객체의 세부 정보를 얻으려면 queryset method 사용해야 한다.

```html
<!--home.html-->
{% for blog in blogs.all %}
    <h1>{{blog.title}}</h1>
    <p>{{blog.pub_date}}</p>
    <p>{{blog.body}}</p>
    <br>
    <br>
{% endfor %}
```

```python
# home.html 생성 후
# urls.py
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
]
```

