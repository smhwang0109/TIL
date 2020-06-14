# 04 model, admin

## model

django가 데이터 베이스를 관리하게끔 해줌.

앱 폴더 안에 models.py에 class 형태로 넣는다. 

- class 이름 맨 앞 대문자 표기
- 인자로 models.Model (이를 통해 클래스가 장고의 모델임을 알 수 있음)
- models의 field 들을 써주면 됨



## django와 데이터 베이스 연동시키기

django와 데이터베이스는 별개의 존재이기 때문에 다양한 데이터베이스 선택 가능

settings.py에 보면 초기 값으로 splite3 사용

`SQLite` 는 하나의 파일에 데이터를 저장하여 쉽고 간편하게 사용할 수 있다는 점이 특징이다.

`settings.py` 에서 프로젝트에 사용할 데이터베이스를 지정해줄 수 있으며, 기본적으로 `SQLite3` 을 사용하도록 설정되어 있다.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

  연동시키기 위해 terminal에서 등록

python manage.py makemigrations 앱이름

: 앱 밑에 migrations 폴더 생성하여 django와 데이터베이스를 연동

python manage.py migrate

: 데이터베이스에 최신 models를 적용시킴

데이터베이스는 `SQL` 을 통해 관리된다. `migrate` 명령어는 Python으로 작성된 데이터베이스 변경사항을 `SQL` 로 번역해주는 역할을 한다고 할 수 있다.

python manage.py sqlmigrate 앱이름 migration번호

:  `migration` 이 `migrate` 될 때 실제로 실행되는 `SQL` 명령어를 확인할 수 있다.

ex) python manage.py sqlmigrate blog 0001



앱들이 필요로하는 **데이터베이스 구조를 기록**한 것이 `Migrations` 파일이고, 이를 **데이터베이스에 적용**시키는 것을 `migrate` 한다고 한다.

`migrate` 명령어는 `settings.py` 의 `INSTALLED_APPS` 리스트를 확인하여 리스트에 포함된 앱이 필요로하는 테이블을 데이터베이스에 생성한다.



## admin

model을 관리하는 역할

- admin 계정 만들기
  - python manage.py createsuperuser : user를 생성
  - username, e-mail, password, password(agin) 입력(password 안보이니 입력시 주의!)

- admin에 models 등록하기

  - admin.py에

  - ```python
    from django.contrib import admin
    from .models import Blog(클래스)
    
    admin.site.register(Blog(클래스이름))
    ```

- admin page(127.0.0.1:8000/admin)에 들어가면 블로그글을 만들 수 있다.

- 다 만든 후 제목이 보이게 하려면 models.py에 class Blog 안쪽에

- ```python
  def __str__(self):
      return self.title
  ```



- 서버시간 맞추기

```re
Note: You are 9 hours ahead of server time.
```

라고 쓰여 있는 것을 볼 수 있다.
그렇다. 서버의 시간이 실제 현재시간보다 9시간 느린 것이다.
`Django` 의 서버 시간은 `settings.py` 의 `TIME_ZONE` 변수에 입력된 표준시간 값을 사용한다. 기본값으로는 협정 세계시를 뜻하는 `UTC` 가 입력되어있다.
아래와 같이 입력하여 대한민국 시간으로 바꿔주자.

```
TIME_ZONE = 'Asia/Seoul'
```

------

### 언어 설정

`TIME_ZONE` 변수 바로 위에 있는 `LANGUAGE_CODE` 변수는 `Django` 에서 사용할 언어를 결정한다. 기본값은 영어인 `en-us` 이다.
아래와 같이 입력하면 한글로 바뀐 관리자 페이지를 볼 수 있을 것이다.

```
LANGUAGE_CODE = 'ko-kr'
```

![img](https://nachwon.github.io/img/django_tutorial/admin_kor.png)





*** 참고**

`Django` 의 앱은 크게 `모델 (Model)`, `템플릿 (Template)`, `뷰 (View)` 로 구성이 되어 있으며, 앱이 이렇게 구성되도록 하는 개발 패턴을 `MTV` 패턴이라고 한다. 이에 대해 좀 더 알아보자.

------

### MVC 패턴

어떤 어플리케이션이 `모델(Model)`, `뷰(View)`, `컨트롤러(Controller)` 로 구성되도록 개발하는 방법을 `MVC` 패턴이라고 한다.

> #### Model-View-Controller (MVC)
>
> 모델-뷰-컨트롤러(Model–View–Controller, MVC)는 소프트웨어 공학에서 사용되는 소프트웨어 디자인 패턴이다. 이 패턴을 성공적으로 사용하면, 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시각적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있다. MVC에서 모델은 애플리케이션의 정보(데이터)를 나타내며, 뷰는 텍스트, 체크박스 항목 등과 같은 사용자 인터페이스 요소를 나타내고, 컨트롤러는 데이터와 비즈니스 로직 사이의 상호동작을 관리한다.
> 출처: [위키피디아](https://ko.wikipedia.org/wiki/모델-뷰-컨트롤러)

`MVC` 패턴은 웹 어플리케이션 개발에서 주로 사용되는 `디자인 패턴` 이다.

> #### 디자인 패턴
>
> 프로그램 개발에서 자주 나타나는 과제를 해결하기 위한 방법 중 하나로, 과거의 소프트웨어 개발 과정에서 발견된 설계의 노하우를 축적하여 이름을 붙여, 이후에 재이용하기 좋은 형태로 특정의 규약을 묶어서 정리한 것이다.
> 출처: [위키피디아](https://ko.wikipedia.org/wiki/디자인_패턴)

`MVC` 패턴은 웹 어플리케이션을 크게 `모델`, `뷰`,`컨트롤러` 의 세 부분으로 구분한다.

- **모델**: 데이터베이스나 파일 등의 데이터 소스를 제어한다.
- **뷰**: 모델로부터 제공된 데이터를 반영하여 사용자에게 보여주게 되는 부분이다.
- **컨트롤러**: 사용자의 요청을 파악하여 그에 맞는 데이터를 모델에 의뢰하고, 그것을 뷰에 반영하여 사용자에게 제공한다.

![img](https://nachwon.github.io/img/django_tutorial/MVC.png)

사용자가 `컨트롤러` 를 조작하면, `컨트롤러` 는 `모델` 을 통해 데이터를 가져오고 그 정보를 `뷰` 에 반영하여 다시 사용자에게 돌려주게 된다.
웹 어플리케이션이 이와 같은 동작 과정을 가지도록 개발하는 방법론을 `MVC` 패턴이라고 한다. 이러한 방식으로 개발을 하면 유지보수가 용이하며, 개발 참여자들 간 효율적인 커뮤니케이션이 가능해진다는 이점이 있다.

------

## MTV 패턴

`Django` 에서는 일반적인 웹 프레임워크들의 `MVC` 패턴과는 조금 다른 `MTV` 패턴을 따른다.
`MTV` 패턴은 `모델(Model)`, `템플릿(Template)`, `뷰(View)` 로 구성되어 있으며, **템플릿이 `MVC` 의 뷰 역할**을 하고, **뷰가 `MVC` 의 컨트롤러 역할**을 담당한다.

- 모델은 데이터를 표현하는데 사용되며, Python 클래스 형식으로 정의된다. 하나의 모델 클래스는 데이터베이스에서 하나의 테이블로 표현된다.
- 템플릿은 사용자에게 보여지는 부분만을 담당한다.
- 뷰는 HTTP Request를 받아 HTTP Response를 리턴하는 컴포넌트로, 모델로부터 데이터를 읽거나 저장할 수 있다.