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