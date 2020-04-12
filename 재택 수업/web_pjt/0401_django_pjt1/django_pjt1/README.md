# django_pjt1

## 각 단계별 구현 과정

*** 기본적으로 model을 작성한 후 url->view->template 순서로 작성**

### 1. models.py

#### **구현 과정**

1. 필드를 이용하여 모델을 구성
2. migration 진행
3. createsuperuser를 이용하여 계정을 만들고 admin 페이지에서 볼 수 있도록 설정

#### **알게된 부분**

window에서는 createsuperuser를 하기 위해 winpty를 붙여야 한다.



### 2. urls.py

#### **구현 과정**

1. include를 이용하여 프로젝트이름 폴더 아래의 urls.py에서 앱이름 폴더의 urls.py를 사용 가능하도록 설정
2. community/urls.py에 오타를 조심하며 urlpatterns 작성



### 3. views.py

#### **구현 과정**

1. 함수를 호출하며 가져오는 인자를 잘 고려하였다.
2. ORM을 이용하여 DB를 객체처럼 불러와 사용하였다.

#### **알게된 부분**

views.py의 함수 이름(ex.new)과 urls.py의 url의 이름(ex.new_review)들을 통일시키지 않았더니 중간에 헷갈리는 경우가 있었다.



### 4. templates.py

#### 구현 과정

1. 가장 상단에 templates 폴더를 만들어 base.html을 만든 후 settings.py의 TEMPLATES 부분을 설정하였다.
2. 앱 폴더에 templates/앱이름 폴더를 만들어 멀티 앱 사용에도 용이하도록 하였다.
3. 각 html 파일에 템플릿 언어를 잘 사용하여 작성하였다.

