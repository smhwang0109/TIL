# 01~02 Django 시작하기

## Django 설치

pip install django



## Django 프로젝트 만들기

1. django-admin startproject 프로젝트이름 : 프로젝트 폴더 생성

2. cd 프로젝트 이름
3. python manage.py runserver : 서버 켜기
   - 끄기는 ctrl + c



## Django 앱 만들기

1. python manage.py startapp 앱이름
2. 프로젝트이름 폴더 안에 settings.py 안에 INSTALLED_APPS 리스트에 추가
   - '앱이름.apps.app이름(첫글자 대문자)Config'

\* 참고

- `django.contrib.admin`: 관리자 페이지 제공
- `django.contrib.auth`: 인증 시스템 제공
- `django.contrib.contenttypes`: 컨텐트 타입 프레임워크
- `django.contrib.sessions`: 세션 프레임워크
- `django.contrib.messages`: 메세지 프레임워크
- `django.contrib.staticfiles`: 정적 파일 관리 프레임워크



## HTML 파일 만들기

앱 파일 바로 아래 templates 디렉토리 만들어서 안에 html 파일 생성



## 함수 만들기

함수는 앱파일 안에 view.py에서 정의



## url 설계

- 동작 원리
  - 해당 url 접근 -> views.py 함수 실행 -> html 파일 실행



## SQLite Browser

`SQLite` 데이터베이스를 좀 더 직관적으로 관리할 수 있도록 해주는 GUI 프로그램이 있다.
`SQLite Browser` 이라는 프로그램이며, 아래 링크에서 다운받아 설치할 수 있다.
[SQLiteBrowser](http://sqlitebrowser.org/)

이 프로그램을 통해서 우리가 생성한 테이블을 직접 확인해볼 수 있다.
`SQLite Browser` 를 실행한 뒤 `데이터베이스 열기(O)` 를 클릭하면 아래의 창이 나타난다.

![img](https://nachwon.github.io/img/django_tutorial/dbsqlite3.png)

`myproject` 폴더의 `db.sqlite3` 파일을 연다.

![img](https://nachwon.github.io/img/django_tutorial/dbbrowser.png)

테이블들이 생성되어 있는 것을 확인할 수 있다.

`SQLite Browser` 를 켠 다음, 프로젝트 폴더 내의 `db.sqlite3` 파일을 열고, `데이터 보기` 항목의 `테이블(T)` 드롭다운 메뉴에서 `blog_post` 를 지정해주면 `Post` 모델의 데이터들을 조회할 수 있다.

![img](https://nachwon.github.io/img/django_tutorial/ORM_Test_added.png)

제일 아래에 `ORM Test` 라는 제목의 `Post` 객체가 들어가있는 것을 볼 수 있다.