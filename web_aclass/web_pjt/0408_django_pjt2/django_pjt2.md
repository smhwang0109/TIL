# Django Pjt 2

## 1. 목표

- CRUD(Create, Read, Update, Delete) 기능 구현
- ModelForm을 이용한 django form 기능 사용
- `GET`과 `POST` 요청을 구분하여 django스럽게 구현



## 2. 프로젝트 개요

영화 리뷰 게시판으로 `ModelForm`과 `GET`, `POST` 메서드를 활용하여 CRUD 기능이 잘 나타나도록 구현



## 3. 세부기능

> setting -> model, form -> url -> view -> template 순서로 작성

### (1) settings.py

> `INSTALLED_APPS` 와  `TEMPLATES` 에 추가

```python
# django_pjt2/settings.py

INSTALLED_APPS = [
    'community', # 앱 추가
    'django_extensions', # ORM 사용을 위해 shell_plus 추가
    'bootstrap4', # django-bootstrap 추가
    # ...생략...
]

TEMPLATES = [
    {
        # ...생략...
        # 최상위에 templates를 만들어 파일을 불러올 수 있도록 추가
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        # ...생략...
    }
]
```



### (2) models.py

> db의 항목들을 class와 field를 이용하여 형식을 정해주고 설정
>
> 저번 django_pjt1과 거의 동일한 요소로 구성

#### 새로 추가된 점

```python
# community/models.py

# ...생략...

def __str__(self):
        return f'title = {self.title}, movie_title = {self.movie_title}, content = {self.content}'
```

ORM을 조금 더 잘 활용해보기 위해 ORM의 출력을 다듬었다.



### (3) forms.py

> models.py에서 작성된 field들을 토대로 사용자에게 입력을 받을 수 있도록 폼을 생성
>
> 이번 프로젝트의 주된 기능으로 새롭게 알게 된 점들이 많았다.

#### 새로 추가된 점

```python
# community/forms.py

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='제목',
        help_text='100자 이내로 작성',
    )
    movie_title = forms.CharField(
        max_length=30,
        label='영화 제목',
        help_text='30자 이내로 작성',
    )
    rank = forms.IntegerField(
        label='평점',
        help_text='0~5점 사이로 작성',
        widget=forms.NumberInput(
            attrs={
                'min':0,
                'max':5,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder':'내용을 입력하세요.'
            }
        )
    )
    class Meta:
        model = Review
        fields = '__all__'
```

- forms를 이용한 폼 생성

model에서 생성한 field를 이용해 폼을 생성하기 위해 django의 forms에서 `ModelForm`을 사용하였다. `ModelForm`을 사용하기 위해서는 class Meta를 설정하여 어떤 model을 사용할지, 어떤 필드를 사용할지를 설정해야 한다.

- forms의 세부 설정들

  1. `label` : html의 label 태그에 들어갈 이름

  2. `help_text` : input 창 근처에서 입력을 도와주기 위한 문구들

  3. `widget`의 `attrs`를 이용하여 class를 만들어주거나 특정 속성들을 생성할 수 있다.

     

  \* 주의 : forms에는 `TextField`가 없기 때문에 `CharField`를 이용한 후 `widget`에서 `Textarea`를 설정해줘야한다.



### (4) urls.py

> url들을 설정하여 웹의 전체적인 경로를 지정
>
> include를 이용하여 각 앱들의 urls.py를 포함하여 사용

#### 새로 추가된 점

```python
# community/urls.py

from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/update', views.update, name='update'),
    path('<int:review_pk>/delete', views.delete, name='delete'),
]
```

`app_name`과 `name`속성을 이용하여 url 경로가 바뀌어도 template에서 바꿀 필요가 없도록 설정



### (5) views.py

> url을 통해 전달된 요청들을 처리
>
> 이번에 새로 알게 된 `GET`과 `POST`를 이용하여 처리하였다.

#### 새로 추가된 점

```python
# community/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Review
from .forms import ReviewForm
```

새롭게 추가된 모듈들이 많다.

우선 CRUD 기능에 맞춰 나눠보았다.

#### Read

```python
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'community/review_list.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review':review
    }
    return render(request, 'community/review_detail.html', context)
```

기존과 크게 달라진 점은 없지만 `get_object_or_404`를 이용해 존재하지 않는 pk 값에 접근했을 때 개발자의 잘못을 나타내는 500대 에러가 아닌 사용자의 잘못을 나타내는 404 에러를 발생시킨다.



#### Create

```python
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)
```

기존 URL로 정보를 전송하던 `GET` 방식의 위험성에 반해 `GET`일 때는 `form`의 양식만 가져오고 `POST` 방식으로 정보를 받는 방법을 진행하였다. `request.POST`안에 있는 사용자들이 입력한 값을 받아와 `form.is_valid`를 통해 유효성을 검증하고 유효하지 않으면 다시 `context`에 `error`를 포함한 `form`을 넣어 보내고 유효한 경우 값을 저장한 후 상세페이지로 `redirect`된다.



#### Update

```python
def update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid:
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)
```

Create에서 사용했던 방법과 같지만 `instance`를 넣어 기존 db에 있는 값을 불러와 넣은 채로 `form`을 만들어 놓는다.



#### Delete

```python
@require_POST
def delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return redirect('community:index')
```

기존과 유사하게 삭제를 하지만 `GET`을 사용하면 URL을 통해 db를 삭제가 가능하기 때문에 `@require_POST` 데코레이터를 이용하여 POST 요청일 때만 삭제가 되도록 한다.



### (6) templates

> 실제 화면에 보이는 화면 구성
>
> review_list.html은 기존과 비슷하여 생략하였습니다.

#### base.html

```html
<!--templates/base.html-->
<!DOCTYPE html>
{% load bootstrap4 %}
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Movie Community</title>
  {% bootstrap_css %}
</head>

<body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="{% url 'community:index' %}"><strong>Moview</strong></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        {% block navbar %}
        {% endblock %}
      </ul>
    </div>
  </nav>
  <div class="container mt-5">
    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>
```

기존과 거의 유사하지만 django-bootstrap 패키지를 이용하여 bootstrap을 넣어보았다.



#### review_detail.html

```html
<!--community/templates/community/review_detail.html-->
<!--생략-->
<form class="d-inline my-2" action="{% url 'community:delete' review.pk %}" method="POST">
  {% csrf_token %}
  <button class="btn btn-secondary">삭제</button>
</form>
<!--생략-->
```

다른 부분은 이전과 비슷하지만 삭제버튼을 `form`안에 넣어 `POST method`로 보내 보안을 강화하였다.



#### form.html

```html
<!--community/templates/community/form.html-->
{% extends 'base.html' %}

{% load bootstrap4 %}

{% block navbar %}
  <li class="nav-item">
    <a class="nav-link" href="{% url 'community:index' %}">Home</a>
  </li>
  <li class="nav-item active">
    <a class="nav-link" href="{% url 'community:create' %}">New <span class="sr-only">(current)</span></a>
  </li>
{% endblock %}

{% block content %}
  <div class="row border rounded py-3 mb-3">
    {% if request.resolver_match.url_name == 'create' %}
    <h2>리뷰 작성</h2>
    {% else %}
    <h2>리뷰 수정</h2>
    {% endif %}
  </div>

  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-dark">작성 완료</button>
  </form>
{% endblock %}
```

1. `request`의 `resolver_match`를 사용하여 `url_name`이 `create`와 `update`를 나눠 표현되는 헤드라인을 다르게 분기하였다.

2. `csrf_token`으로 토큰을 확인하여 보안을 강화하였다.

3. `context`를 통해 넘어온 `form`에서 양식을 받아 bootstrap으로 표현하였다.

   