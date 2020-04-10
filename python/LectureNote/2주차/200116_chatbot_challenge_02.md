# 챗봇 챌린지 day2 (2020.01.16.)

## 1. 환경 설정

### 1) 파이썬 실행 방법

1. IDLE ( Development Learning Environment)

- line by line 으로 실행

2. CMD

- 윈도우라는 운영체제를 조작하기 위한 터미널 창
- ''명령어' 인터페이스

3. Shell Emulator

- CMD와 비슷하지만 리눅스 운영체제에 보다 가까움



### 2) Git 설치

- [공식 홈페이지](https://git-scm.com/download/win)
- Default 옵션으로 설치
- Launch Git Bash 선택하여 종료



### 3) Shell Emulator 명령어

```shell
$ pwd # presend working directory (/c/Users/multicampus)
$ ls # listing # cmd 에서는 dir

$ cd [폴더명] # change directory (폴더명 앞 부분 타이핑하고 tap키로 자동완성)
$ cd .. #  상위 폴더로 이동
$ cd ~ # 홈 디렉토리로 이동
$ mkdir [폴더명] # make directory

$ code # code editor 오픈
$ code . # 현재 폴더에서 code editor 오픈

$ python [실행할 파일명] # 파이썬에게 해당 파일 실행을 명령 (자동완성)

$ pip install [설치할 패키지명] # 패키지 설치
$ pip list # 설치된 패키지 리스트 출력

$ clear
```

- **홈 디렉토리** : 접속하자마자 나오는 디렉토리, `~` 표시로 표현 (ex. `~/Downloads`)
- **패키지**: 외부에 있는 코드 묶음



#### * 환경변수 조작

- 내 PC - 속성 - 고급 시스템 설정 - 고급 - 환경 변수 - 위/아래 탭에서 Path 편집



### 4) VS Code

- Linter 프로그램 : 설치하면 스타일을 맞춰 줌
- `Ctrl + F5` : 코드 실행



## 2. 파이썬 활용

### 1) 브라우저 조작

```python
import webbrowser # 모듈

base_url = 'https://search.naver.com/search.naver?query='

programs = ['나혼자산다', '뭉쳐야찬다', '슈퍼맨이 돌아왔다']

for program in programs:
    webbrowser.open(base_url + program)
```

*파이썬에서는 홑따옴표가 컨벤션 (자바스크립트에서는 쌍따옴표가 컨벤션)*

- URL 파헤치기

  > https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=ssafy&oquery=ssasfy&tqi=Um%2B3pdprvTosseGn2Sdssssss7s-474006
  >
  > 의 본질은
  >
  > https://search.naver.com/search.naver?query=ssafy



### 2) 웹 스크래핑

~~웹 스크래핑과 크롤링은 완전히 다른 개념~~

#### (1) requests : 페이지 소스 얻기

- 개발자도구 - 네트워크 - 특정 요청 - Headers
  - Remote Address : 해당 서버의 본질적인 식별자
  - Request URL: Remote Address의 인간 버전
    - DNS (Domain Name Server) : URL 만들어주는 서버

```shell
$ pip install requests # requests 패키지
```

```python
import requests # HTTP 요청을 보내는 모듈

url = 'https://finance.naver.com/sise/'
response = requests.get(url) # 요청에 대한 응답 결과를 반환

print(response) # 응답 상태 출력
print(response.text) # 응답 내용 출력
```

- **<Response [200]>** : pass
- **<Response [400]>** : 요청자쪽 잘못이 대부분
- **<Response [500]>** : 응답자쪽 잘못이 대부분
- **응답 내용** : 페이지 소스와 동일



#### (2) parsing : 필요한 정보만 찾기 via beautifulsoup

```shell
$ pip install bs4 # HTML 또는 XML 파일에서 데이터를 추출하기 위한 라이브러리
$ pip install lxml # HTML 또는 XML 을 파이썬이 이해할 수 있도록 변환하기 위한 라이브러리
```

```python
data = bs4.BeautifulSoup(response, 'lxml') # 응답 내용을 lxml 이라는 parser를 통해 파이썬이 해석 가능하게 변환하여 반환

kospi = data.select_one('#KOSPI_now').text # id 기반으로 html 문서를 검색한 후 내부 텍스트만 반환
kosdaq = data.select_one('#KOSDAQ_now').text

print(f'KOSPI: {kospi}, KOSDAQ: {kosdaq}')
```

- **html** : 검색이 용이한 DOM tree 구조를 갖는 문서

- 스크래핑 하고자 하는 부분에서 [ 우클릭 - 검사 - copy - copy selector ] 로 선택자를 쉽게 얻을 수 있음

  

#### * 실습

- 네이버 원/달러 환율 가져오기
- 다음 실시간 검색어 1-10위 가져오기

```python
import requests
import bs4

url = 'https://www.daum.net/'
response = requests.get(url).text
data = bs4.BeautifulSoup(response, 'lxml')

keywords = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a') # select 반환값: list 타입은 아니지만 비슷하게 사용할 수 있도록 되어있음

for idx, item in enumerate(keywords):
   print(f'{idx+1}위 검색어: {item.text}')
```



### 3) API 사용

> Application Programming Interface (Interface: 접면)
>
> 서로 다른 시스템이 프로그래밍을통해 서로의 접면에 접근하여 커뮤니케이션하는 방식

- 모든 웹 서비스 상의 소통 방식은 다음과 같음
  - 요청 Request: URL
  - 응답 Response: HTML, XML, JSON, ...

- API를 통해서는 데이터만을 가져옴 (주로 JSON 타입)

```python
import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
# time = '893'
time = input("몇 회차 로또 당첨 번호를 알고 싶으세요? ")
response = requests.get(url+time).json()
### requests.get(url).json 은 dictionary 타입으로 반환
### requests.get(url).text 는 string 타입으로 반환

winner = []
for i in range(1, 7):
    num = response[f'drwtNo{i}']
    winner.append(num)

print(f'당첨번호: {sorted(winner)}')

lotto = random.sample(range(1, 46), 6) # 비복원추출
print(f'선택번호: {sorted(lotto)}')

won = 0
for _ in range(1000):
    lotto = random.sample(range(1, 46), 6)
    '''
    matched = 0
    for num in lotto:
        if num in winner:
            matched += 1
        continue   
    '''
    matched = len(set(winner) & set(lotto)) # 교집합
    if matched >= 3:
        won +=1
        print(f'당첨입니다! {matched}개 맞췄습니다!')

print(f'10,000회 중 {won}회 당첨되었습니다. 끝!')
```

[로또 API by 동행복권](https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=819)

[JSON 뷰어 크롬 익스텐션](https://chrome.google.com/webstore/detail/json-viewer/aimiinbnnkboelefkjlenlgimcabobli)



### 4) Flask

#### (1) Flask 구동

```shell
$ pip install Flask
$ pip list

# 아래 코드 작성 후

$ flask run

# 코드 변경시 ctrl + c 로 서버 종료 후 재시작
```



#### (2) Flask 기초

```python
# app.py 파일명 지켜야 함
from flask import Flask

app = Flask(__name__)

@app.route('/') # 괄호 안에 받아들일 요청 내용('/')을 입력
def home():
    return 'happy hacking!'

@app.route('/ssafy')
def ssafy():
    return 'happy ssafy!'

### variable routing
@app.route('/hello/<name>') # <> 표시는 변할 수 있는 값이라는 의미
def hello(name):
    return 'hello ' + name

# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
'''
### 사용자 입력값은 기본적으로 string으로 들어옴
@app.route('/cube/<num>') 
def cube(num):
    return str(int(num)**3)
'''
@app.route('/cube/<int:num>') # 기본적으로 형 변환을 해서 받음
def cube(num):
    return str(num**3)
```

- **app.py** : 파일명 동일하게 해야함
- 파이썬에서 `__??__` 와 같은 표현은 파이썬 상에서 사용하기 위해 시스템이 만들어 놓은 경우가 대부분.. (추후 설명)
- `http://127.0.0.1:5000/` : 콜론 뒤의 5000은 포트 넘버 (추후 공부)
- `@` 데코레이터 라는 문법 (추후 설명)
- `<variable>` : **variable routing** 이라고 하며 interactive 하게 반응



```python
from flask import Flask
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def home():
    return 'happy hacking!'

@app.route('/newyear')
def newyear():
    now = datetime.datetime.now()
    month = now.strftime("%m")
    day = now.strftime("%d")
    if month == 1 and day == 1:
        return "설날임"
    else:
        return "설날아님"
```

[is it christmas](https://isitchristmas.com/)

[표준 라이브러리 datetime](https://docs.python.org/ko/3/library/datetime.html)



#### (3) HTML

HyperText Markup Language

- `! + tap` 으로 기본 템플릿 자동완성 가능

```html
<!-- home.html -->

<!DOCTYPE html>
<html>
    <head>
        <title>Eunjung Jenny</title>
    </head>
    <body>
        <h1>전은정의 페이지다.</h1><hr>
        <h2>와우와우</h2><hr>
        <h3>와우와우</h3><hr>
        <h4>와우와우</h4><hr>
        <h5>와우와우</h5><hr>
        <h6>와우와우</h6><hr>
        
        <p>오늘 드디어 간식이 나온다. 신난다. 룰루랄라</p>
        <a href="https://edu.ssafy.com/comm/login/SecurityLoginForm.do" target="_blank">출첵은 중요해</a>
        
        <ul>
            <li>Javascript</li>
            <li>C</li>
            <li>Python</li>
        </ul>
        
        <h2>검색 다모아</h2>
        <h3>네이버</h3>                
        <form action="https://search.naver.com/search.naver">
            <input type="text" name="query">
            <input type="submit">
        </form>
        <h3>다음</h3>                
        <form action="https://search.daum.net/search">
            <input type="text" name="q"> 
            <input type="submit">
        </form>
        <h3>구글</h3>                
        <form action="https://google.com/search">
            <input type="text" name="q">
            <input type="submit">
        </form>
    </body>
</html>
```

- input 태그의 name 속성은 입력된 정보(parameter)를 담아서 보내는 **박스의 이름**



#### (4) Flask 와 HTML

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/html')
def html():
    return render_template('home.html') ### html 문서를 넘김
```

- flask 에 넘겨주고자 하는 html 파일은 **templates 폴더** 에 위치해야 함
- **render_template** 매소드는 html 파일을 렌더링



```python
# app.py : 파일명 동일해야 함

from flask import Flask, render_template, request
from datetime import datetime
from faker import Faker

app = Flask(__name__)
fake = Faker('ko_KR') 

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

@app.route('/result')
def result():   
    user = request.args.get('user')  # pastlife에서 사용자 이름을 받음
    # print(user) # 작동 확인용: 콘솔에 출력됨
    job = fake.job()
    return render_template('result.html', user=user, job=job) # user 정보를 html에 보내어 렌더링
```

- **request 매소드** : flask 내부적으로 가지고 있는 정보함 (확인해보기)

[Faker](https://github.com/joke2k/faker)



```html
<!--pastlife.html-->
<!DOCTYPE html>
<html>
  <head>
    <title>당신의 전생은...?</title>
  </head>
  <body>
    <h1>당신의 전생은?!</h1>
    <p>당신의 전생을 알려드립니다...</p>
    <form action="/result"> <!-- 홈 주소 뒤에 붙게 됨 -->
      <input type="text" placeholder="이름을 입력해주세요." name="user">
      <input type="submit">
    </form>
  </body>
</html>
```

```html
<!--result.html-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!--모바일 지원-->
  <meta http-equiv="X-UA-Compatible" content="ie=edge"> <!--익스플로러 지원-->
  <title>당신의 전생은 바로!</title>
</head>
<body>
  <h1>{{ user }}님의 전생은 {{ job }}입니다.</h1> <!-- 렌더링시 받아올 정보는겹중괄호 안에 위치 -->
</body>
</html>
```

=> `jenny.pythonanywhere.com` 에서 확인 가능

- 입력창에 이름 입력시 URL 형태

  `http://127.0.0.1:5000/result?user=%EC%A0%84%EC%9D%80%EC%A0%95](http://127.0.0.1:5000/result?user=이름`

  

------

##### 네이버 접속시 발생하는 이벤트

- 네이버 url 을 주소창에 입력하면 Remote Address 를 보낸다.

-----------

##### 참고 사이트

[더브이씨, 한국 스타트업 투자 데이터베이스](https://thevc.kr/) : 회사 정보 확인 (스타트업의 가치는 일반적으로 투자유치액의 약 10배)

[python anywhere](https://www.pythonanywhere.com/) : 파이썬을 활용한 웹앱 배포

_______________



# 끝

