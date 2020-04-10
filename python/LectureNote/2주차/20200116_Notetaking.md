# 20200116 배운 점!



## 오전: Python 심화



### 1. 컴퓨터조작, 웹스크래핑, 파일명 바꾸기

___

#### 1-1) 컴퓨터 조작하기

##### 웹 브라우저를 조작하기

###### **Python Idle: Interactive Development Learning Environment**

```python
>>> print('hello')
hello
```

* 런타임에서 바로 실행결과를 확인할 수 있다.



**웹에있는 정보를 가져오는건 크게 2가지**

* willingly 주고 싶어해서 API를 통해 가져오거나
* 정보제공자가 원하지 않음에도 사용자가 긁어오는 것이 스크래핑



###### Shell Emulator (Git)

* 30년전에는 지금 존재하는 그래픽 인터페이스가 존재하지 않았음! 과거에는 터미널을 통해 사용

  * 명령어 인터페이스에 익숙해지자.

* Shell Emulator 다운로드 (Git)

  * Downloads: 2.25.0 버전 설치 (default옵션으로 설치)

* 명령어

  * 리눅스에서 **홈 디렉토리**는 ~ (물결 표시): c/Users/multicampus
  * ls: list (윈도우에서는 dir)
  * pwd: print working directory
  * cd(change directory): directory=폴더와 같은 말!
    * 앞으로는 모든 폴더명을 다 치지말고 `앞 두세글자만 쓰고 + Tab`
    * cd를 하면 노란색으로 파일 디렉토리 나옴

  * cd .. : 상위 폴더로 이동
  * . : 현재 폴더
  * cd ~ : 절대적인 위치로 바로 이동하는 방법
  * mkdir: make directory
    * 폴더 만들기
  * code: 코드 에디터 불러오기

* python파일의 확장자는 .py이다!
* python 관련 명령어
  * python -- version: 파이썬 버전 확인하기
  * python 파일명 : 파일이 실행된다



###### 파이썬에서 브라우저 조작 방법

하나의 브라우저 오픈하기

* ```python
  import webbrowser
  
  webbrowser.open('https://www.naver.com') #웹브라우저 열기!
  #url= uniform resource locator
  ```



여러 브라우저 오픈하기

* ```python
  import webbrowser
  
  base_url = 'https://search.naver.com/search.naver?query='
  
  words=['아이유','수지','설현']
  url1 = base_url+words[0]
  url2 = base_url+words[1]
  url3 = base_url+words[2]
  webbrowser.open(url1)
  webbrowser.open(url2)
  webbrowser.open(url3)
  ```



여러 브라우저 오픈하기(간결 버전)

* ```
  import webbrowser
  
  base_url = 'https://search.naver.com/search.naver?query='
  
  words = ['아이유','수지','설현']
  
  for word in words:
      webbrowser.open(base_url+word)
  ```



브라우저 검사

* Network
* Headers (**Remote Address** (`:`전까지 숫자를 주소창에 치면 그대로 나옴~))
* **브라우저는 우리 대신 Request/요청을 보내준다**



##### 웹 스크래핑

* 브라우저의 정보를 가져온다고 해도 무조건 crawling이 아니다!

* `pip`: python 패키지(외부에 있는 코드 묶음)

  * ```
    pip install requests
    python -m pip install --upgrade pip
    pip list
    ```

* 

* ```
  import requests
  url = 'https://www.daum.net'
  response = requests.get(url)
  print(response)
  ```

  * <Response[200]>
    * 200이라는 숫자는 긍정적인 숫자
    * 4로 시작하면 대부분 우리/개발자의 잘못
    * 5로 시작하면 There's a big problem

###### 금융 데이터 가져오기

**Beautiful Soup**

- 문서 파싱 도구로, 파이썬이 문서를 검색하기 쉽게 만들어 주는 도구

  - **`파싱(Parsing)**`: 정보를 구조화 시켜주는 행위를 파싱이라고 함 

- 설치

  - ```
    pip install bs4
    pip install lxml
    ```

* **HTML Dom: Tree**

  * 트리 구조로 검색이 쉽고 빠르다.
  * 밑으로 뻗어나갈 때, 각각의 가지가 20단 정도 되면 정보가 엄청 많아짐 

* HTML

  * `id`: identifier (특정한 정보를 바로 포착할 수 있다)

* 파싱하는 방법

  * ```python
    import requests
    import bs4
    
    url = 'https://finance.naver.com/sise/'
    
    response = requests.get(url).text #html문서
    
    data = bs4.BeautifulSoup(response, 'lxml') #Beautiful soup(html문서) 'lxml'이라는 파서
    
    kospi = data.select_one('#KOSPI_now') #string으로 넣어줘야함
    kosdaq = data.select_one('#KOSDAQ_now')
     
    #print(kospi.text) #kospi 안에 있는 글자만 가져다줘 #"explicitly specified" 경고
    
    print(kospi.text)
    print(kosdaq.text)
    ```

* ID를 찾기 위한 쉬운 방법

  * 원하는 데이터에 커서 올려놓고 -> 우클릭 --> 검사--> 코드에 마우스 커서 올려놓고 --> 우클릭 --> `copy selector`

    

###### 환율 스크래핑

* ```python
  # 기초 실습 : 네이버 금융 원/달러 환율
  
  import requests
  import bs4
  
  url='https://finance.naver.com/'
  
  response = requests.get(url).text
  data = bs4.BeautifulSoup(response,'lxml')
  
  exchangerate = data.select_one('#content > div.article2 > div.section1 > div.group1 > table > tbody > tr.up.bold > td:nth-child(2)')
  
  print(exchangerate.text)
  ```

  

###### 실시간 검색어 스크래핑

* ```python
  #심화 실습 : 다음 실시간 검색어 가져오기
  
  import requests
  import bs4
  
  url = 'https://www.daum.net/'
  
  response=requests.get(url).text
  data=bs4.BeautifulSoup(response,'lxml')
  
  issues = data.select_one('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_mini > ol')
  print(issues.text)
  ```

* ```python
  import requests
  import bs4
  
  url = 'https://www.daum.net/'
  
  response = requests.get(url).text
  
  data = bs4.BeautifulSoup(response, 'lxml')
  date = data.select_one('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > span').text
  
  print(f'{date[5:7]}월 {date[8:10]}일 기준 실시간 검색어\n')
  
  # select
  keywords = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li > div > div:nth-child(1) > span.txt_issue > a')
  
  for idx, item in enumerate(keywords):
     print(f'{idx+1}위 검색어: {item.text}')
  ```

  

* 주석 달기

  * 파이썬에서는 주석을 필요한 곳에만 단다! (C랑 C++ 같은 언어에서는 주석 필수)



# 오후 (API 사용, Flask 서버, HTML)

###### API 사용

* 데이터가 'Json' 형태로 나옴 

* json(javascript object notation) viewer chrome extension

  * json은 dictionary 형태

* ```python
  import requests
  
  # 1. requests를 통해 동행로또 API에 요청을 보내기
  url ='https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=893'
  response = requests.get(url).json() #Dictionary 가 불려져 온다
  
  no1 = response['drwtNo1']
  
  winner = []
  
  '''
  winner.append(response['drwtNo1'])
  winner.append(response['drwtNo2'])
  winner.append(response['drwtNo3'])
  winner.append(response['drwtNo4'])
  winner.append(response['drwtNo5'])
  winner.append(response['drwtNo6'])
  '''
  for i in range(1,7):
      winner.append(response[f'drwtNo{i}'])
  
  print(winner)
  ```

* 로또 당첨될 때 까지 몇번을 해야하나?

  * ```python
    import requests
    import random
    
    # 1. requests를 통해 동행로또 API에 요청을 보내기
    url ='https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=893'
    response = requests.get(url).json() #Dictionary 가 불려져 온다
    
    no1 = response['drwtNo1']
    
    winner = []
    
    for i in range(1,7):
        winner.append(response[f'drwtNo{i}'])
    
    print(winner)
    
    
    lotto=sorted(random.sample(range(1,46),6))
    
    
    for _ in range (100000):
        lotto=sorted(random.sample(range(1,46),6))
        cnt=0
        for w in winner:
            if w in lotto:
                cnt=cnt+1
        if cnt>=5:
            print('3등 이상입니다.')
    
    ```



* 더 smart 한 방법

  * ```python
    import requests
    import random
    
    # 1. requests를 통해 동행로또 API에 요청을 보내기
    url ='https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=893'
    response = requests.get(url).json() #Dictionary 가 불려져 온다
    
    no1 = response['drwtNo1']
    
    winner = []
    
    for i in range(1,7):
        winner.append(response[f'drwtNo{i}'])
    
    print(winner)
    
    lotto=sorted(random.sample(range(1,46),6))
    
    cnt=len(set(lotto)&set(winner))
    
    print(cnt)
    ```



## Flask 서버

* Backend 웹서버

* 아래 명령어로 Flask 프레임워크를 설치하기

  * ```
    cd flask
    code .
    pip install Flask
    ```

* 플라스크 실행하기

  * `Flask run`

  * 재실행 시 터미널에서 `ctrl+c`필요

  * 변수처럼 활용하기 위한 것

    * ```python
      @app.route('/<변수처럼활용가능>') #Handling이 가능해진다
      ```

* 웹사이트 만들기

  * ```python
    from flask import Flask
    
    app = Flask (__name__) #언더바로 시작하는 것은 파이썬이 사용하려고 만든 시스템 언어
    
    @app.route('/') #url을 안에 정의해야함 #/로 항상 시작
    def home(): #루트 페이지
        return 'happy hacking!'
    
    @app.route('/ssafy')
    def ssafy():
        return 'This is SSAFY Page'
    
    @app.route('/hello/<name>') #<>: 변수처럼 활용할 수 있음
    def hello(name):
        return 'Hello '+ name
    
    # /cube/1 => 1
    # /cube/2 => 8
    # /cube/3 => 27
    '''
    @app.route('/cube/<num>')
    def cube(num):
        return "This is the cube of "+num+": "+str(int(num)**3)
    '''
    
    @app.route('/cube/<int:num>')
    def cube(num):
        return str(num ** 3)
    ```

  

* 오늘이 1월 1일인가?

  * ```python
    from datetime import datetime
    from flask import Flask
    
    app = Flask (__name__) 
    
    @app.route('/newyear')
    def newyear():
        today=datetime.now()
        if today.month==1 and today.day==1:
            return "Yes"
        else:
            return "No"
    ```



## HTML

* `<>` 는 Tag라고 불린다.

* HTML 의 기본구조

  * 템플릿 자동완성 기능: `!+tab` 

  * ```html
    <!DOCTYPE html> <!--html 작성할 때는 무조건 써야 함-->
    <html>
        <head>
            
        </head>
        <body>
    
        </body>
    </html>
    ```

* `<hr>`: 선을 그려준다. 그러나 `<hr>`은 닫는 태그가 따로 없다

* `<a href>`: 링크 타고 들어갈 수 있음!

* `<ul>`: Unordered List 불렛 포인트

* `<p>`: 단락을 나눌 때 사용한다.

* `<input>`: 입력창을 띄워준다 (`<input type= "text">`)

* 간단한 홈페이지 만들기

  * ```html
    <!DOCTYPE html> <!--html 작성할 때는 무조건 써야 함-->
    
    <meta charset='utf-8'>
    
    <html>
        <head>
            <title>Lin's Homepage</title> <!--웹브라우저 탭에 나타나는 명칭-->
        </head>
        <body>
            <h1>Lin Shin</h1> <!--h stands for header-->
            <hr>
            <p> 안녕하세요. SSAFY 서울 1반 CA 신채린입니다. </p>
            <a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp">SSAFY</a> <!-- href= hyper reference-->
            <ul>
                <li>Python</li>
                <li>Java</li>
                <li>Javascript</li>
            </ul>
    
            <h2>검색 다 모아</h2>
    
            <h3>네이버</h3>
                <form action="https://search.naver.com/search.naver"> <!--입력을 받고 행동을 정의하는 것이 form 태그에서 일어남-->
                    <input type="text" name="query"> 
                    <input type="submit">
                </form>
    
            <h3>다음</h3>
                <form action="https://search.daum.net/search"> 
                    <input type="text" name="q"> 
                    <input type="submit">
                </form>
    
            <h3>구글</h3>
                <form action="https://www.google.com/search"> <!--입력을 받고 행동을 정의하는 것이 form 태그에서 일어남-->
                    <input type="text" name="q"> 
                    <input type="submit">
                </form>
    
        </body>
    </html>
    ```

  

* Flask에 html 넣어도 작동할까?

  * Html 팀플릿을 만들어준다

    * ```
      from flask import Flask, render_template
      ```



### 당신의 전생은?

* Fake

  * from faker import Faker

  * ```python
    from faker import Faker
    fake = Faker('ko_KR')
    ```

* app.py

  * ```python
    from datetime import datetime
    from flask import Flask, render_template, request #render template: html 템플릿을 만들어준다. #request: Flask안에 들어가는 객체
    from faker import Faker
    
    app = Flask (__name__) #언더바로 시작하는 것은 파이썬이 사용하려고 만든 시스템 언어
    fake = Faker('ko_KR')
    
    @app.route('/') #url을 안에 정의해야함 #/로 항상 시작
    def home(): #루트 페이지
        return 'happy hacking!'
    
    @app.route('/ssafy')
    def ssafy():
        return 'This is SSAFY Page'
    
    @app.route('/hello/<name>') #<>: 변수처럼 활용할 수 있음
    def hello(name):
        return 'Hello '+ name
    
    # /cube/1 => 1
    # /cube/2 => 8
    # /cube/3 => 27
    '''
    @app.route('/cube/<num>')
    def cube(num):
        return "This is the cube of "+num+": "+str(int(num)**3)
    '''
    
    @app.route('/cube/<int:num>')
    def cube(num):
        return str(num ** 3)
    
    #datetime
    @app.route('/newyear')
    def newyear():
        today=datetime.now()
        if today.month==1 and today.day==1:
            return "Yes"
        else:
            return "No"
    
    @app.route('/html')
    def html():
        return render_template('home.html') #Flask의 약속에 의해 html은 폴더 안에 있어야 한다.
    
    @app.route('/pastlife')
    def pastlife():
        return render_template('pastlife.html') 
    
    @app.route('/result')
    def result():
        #pastlife/로부터 넘겨진 사용자의 이름을 받아온다.
        user = request.args.get('user') #argument는 기본적으로 dictionary의 형태로 넘어온다.
        job=fake.job()
        return render_template('result.html', user=user, job=job) #user=user 템플릿에서 user라는 변수명으로 user값을 쓸게.
        
    ```

    

* result.html

  * ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>당신의 전생은!!</title>
    </head>
    <body>
        <h1>{{ user }}님의 전생은 {{ job }}입니다.</h1>
    </html>
    ```

  

* pastlife.html

  * ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>당신의 전생은?</title>
        </head>
        <body>
            <h1>당신의 전생은?!</h1>
            <p>당신의 전생을 알려드립니다.</p>
    
            <form action="/result">
                <input name="user" placeholder="이름을 입력해주세요." type="text">
                <input type="submit">
            </form>
        </body>
    </html>
    ```

* home.html

  * ```html
    <!DOCTYPE html> <!--html 작성할 때는 무조건 써야 함-->
    
    <meta charset='utf-8'>
    
    <html>
        <head>
            <title>Lin's Homepage</title> <!--웹브라우저 탭에 나타나는 명칭-->
        </head>
        <body>
            <h1>Lin Shin</h1> <!--h stands for header-->
            <hr>
            <p> 안녕하세요. SSAFY 서울 1반 CA 신채린입니다. </p>
            <a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp">SSAFY</a> <!-- href= hyper reference-->
            <ul>
                <li>Python</li>
                <li>Java</li>
                <li>Javascript</li>
            </ul>
    
            <h2>검색 다 모아</h2>
    
            <h3>네이버</h3>
                <form action="https://search.naver.com/search.naver"> <!--입력을 받고 행동을 정의하는 것이 form 태그에서 일어남-->
                    <input type="text" name="query"> 
                    <input type="submit">
                </form>
    
            <h3>다음</h3>
                <form action="https://search.daum.net/search"> 
                    <input type="text" name="q"> 
                    <input type="submit">
                </form>
    
            <h3>구글</h3>
                <form action="https://www.google.com/search"> <!--입력을 받고 행동을 정의하는 것이 form 태그에서 일어남-->
                    <input type="text" name="q"> 
                    <input type="submit">
                </form>
    
        </body>
    </html>
    ```

    





***TIP***

* thevc.kr (회사가 어느 정도인지 보임)

  * 30억+를 투자 받았다면 회사의 가치는 *10의 정도!
  * risky하지 않은 회사는 100억 이상 투자 받은 회사

* 네이버, 카카오에서 가장 빈번하게 묻는 질문: naver.com/daum.net에 들어갔을 때 나오는 내용을 천천히 기술하시오

  * 1. naver.com 이라는 주소를 가진 것에 요청하기

       

* 하이라이징 startup에 들어가면 빠르게 성장하는 개발자가 가능

  * 토스
  * 카카오 (카카오 뱅크)
  * 뱅크샐러드

* Main reference="공식문서"





