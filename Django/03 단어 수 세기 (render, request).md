# 03 단어 수 세기

## render

- 최대 3개 인자까지 받을 수 있다.
  - request, html 파일과 같은 템플릿, dictionary형 인자



## 템플릿 언어

html파일에서 urls.py 에서 지정해준 링크로 가는 법

```html
<a href="{%url 'home'%}">Home</a>
```



## request

request.GET['받아올 name']





#### How Django processes a request

한 사용자가 `Django` 웹 페이지를 호출하면, `Django` 는 아래의 알고리즘을 거쳐 어떤 Python 코드를 실행할지 결정한다.

1. 먼저 어떤 `URLconf` 모듈을 사용할지 결정한다. 보통의 경우, `settings.py` 의 `ROOT_URLCONF` 변수에 정의되어 있는 모듈을 사용한다. 우리의 경우 `config.urls` 모듈이다.
2. 해당 `URLconf`, 즉, 우리의 경우 `config` 폴더안의 `urls.py` 모듈에서 `urlpatterns` 라는 리스트 객체를 찾는다. 이 리스트 객체는 `django.conf.urls.url()` 의 인스턴스인 `url` 객체들의 리스트이다.
3. 이 `urlpatterns` 리스트안의 `url` 객체들을 순서대로 하나씩 순회하면서 각 객체가 가진 정규표현식을 호출된 웹 페이지의 `URL` 주소와 매칭시킨다.
4. 정규표현식들 중 하나와 매치가 되는 순간 순회를 멈추고 매치된 정규표현식을 가진 `url` 객체의 `view` 를 실행시킨다.
5. 만약 매칭되는 정규표현식이 없거나, 어떤 다른 예외가 이 과정 중에 발생할 경우 상황에 적합한 에러 메세지를 리턴한다.