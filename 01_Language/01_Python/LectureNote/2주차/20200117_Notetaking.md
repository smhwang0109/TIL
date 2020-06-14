# 2020월 1월 17일

## 오전

## Flask

- 복습

  - `app.route()`: 주문을 받기 위함

    - 그 아래쪽에 def는 주문을 어떻게 처리할지 작성

  - `render_template()`: html 문서를 보내주기 위함이다. (import를 해야한다.)

  - `! + Tab`: html 구조 자동완성

  - json: 정보를 주고받을 때 하나의 표현 양식 (Python dictionary와 비슷하게 생겼다.)

  - `xml` : 데이터가 담긴 문서

    

- **Auto Load**를 하기 위해서는?

  - ```python
    if __name__== '__main__':
        app.run(debug=True)
    ```

- Run 하기 위해서는 `python 파일명.py` 

  

- ### 미세먼지 서비스

  - api 가져오기 (data.go.kr에서)

  - ```python
    @app.route('/dust')
    def dust():
    
        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=xlBqwAl%2BR3JMCwJ39tSRyKbvXJQOlWTHUg%2BeW370uq0nJ5I0YMboZn1hwjKl6ha%2FRY7allB7ksMt8Ud2%2FNLj5g%3D%3D&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'
        request = requests.get(url).text
        soup = BeautifulSoup(request,'xml')
        item = soup('item')[5]
        time = item.dataTime.text
        dust = int(item.pm10Value.text)
        return render_template('dust.html', dust=dust)
    ```



* ### 텔레그램 챗봇 만들기

  * #### 텔레그램 API 문서

    * https://core.telegram.org/bots/api

    * making requests

      * ```
        https://api.telegram.org/bot<token>/METHOD_NAME
        ```

        * Web Browser에 위 주소를 쳐보면 (token 넣은 상태에서) 나의 정보를 알려준다.

      * GET and POST를 Support한다.

    * Method (되도록이면 대소문자를 구분해야 한다.)

      * getMe: 내 정보

      * getUpdates: 봇의 현재 상태를 알려준다. 봇 안에서 어떤 메시지들이 오갔는지 알려준다. 그리고 누가 이 봇에 메시지를 보냈는지 알 수 있다.

      * setWebhook

      * sendMessage

        * Parameters: 메시지를 주소창에 실어서 보내야한다. (0116 검색창, 전생찾기에서 해 봄!)

        * chat_id: unique identifier for target chat

        * ```
          https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat id>&text=<text>
          ```

  * #### 메시지 보내기

  * ```python
    import requests
    from pprint import pprint
    
    base_url = 'https://api.telegram.org'
    key = '926776064:AAE28UUN9xgJTZ7SXWrmhPbggVyGz8Kk_us'
    
    update_url = f'{base_url}/bot{key}/getUpdates'
    
    
    
    #1. chat_id 받아오기
    ## -chat_id 하나만 받아오기 (첫번째)
    # response = requests.get(update_url).json()
    # chat_id = response['result'][0]['message']['chat']['id']
    # print(chat_id)
    #pprint.pprint(chat_id) pprint는 예쁘게 프린트해주는 것
    
    ##chat_id 전부 가져오기
    response=requests.get(update_url).json()
    
    chat_ids=[]
    text="Hello"
    
    for result in response['result']:
        chat_ids.append(result['message']['chat']['id'])
    
    setofids=set(chat_ids)
    
    for i in setofids:
        message_url=f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}'
        requests.get(message_url)
        
    
    #pprint(len(response['result']))
    
    ```

    

## 오후

### Webhook

* 상태변화에 대한 메시지 받기

* 웹에서 '상태 변화'가 있다는 점을 인터넷을 통해 하나의 '요청' (Request) 형태로 오기 때문에, 이 요청을 받을 서버가 필요하다.

* Webhook을 작성할때 URL이 필수로 필요하다.

  * Set Webhook --> 어디로 요청을 받을 건지 알기 위해서 URL (즉, 서버 주소)을 넣어야 한다.

* **ngrok**: 요청을 대신 받아주는 곳이며, 우리는 ngrok한테 전달받는다.

  * 서버가 대신해서 Telegram에서 받고, 다시 우리에게 가져다준다.

  * 무조건 cmd 창에서 실행해야 한다.

  * 1. Cmd창

    ```bash
    ngrok http 5000 
    ```

  * 2. 입력하면 Forwarding에 있는 주소를 메모장을 켜서 저장한다.

  * Telegram 챗봇이 ngrok에 요청하는 것!

    * ```
      @app.route('/telegram', methods=['POST'])
      ```

* 메아리 보내기

  * ```python
    from flask import Flask, render_template , request
    import requests
    from pprint import pprint
    
    app=Flask(__name__)
    
    base_url = 'https://api.telegram.org'
    key = '926776064:AAE28UUN9xgJTZ7SXWrmhPbggVyGz8Kk_us'
    update_url = f'{base_url}/bot{key}/getUpdates'
    #message_url = f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}'
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/send')
    def send():
        response = requests.get(update_url).json()
        chat_id = response['result'][0]['message']['chat']['id']
        text= request.args.get('msg')
        message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(message_url)
        return '메시지를 전송하였습니다'
    
    @app.route('/telegram', methods=['POST'])
    def telegram():
        response=request.get_json()
        text = response['message']['text']
        chat_id = response['message']['chat']['id']
        message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(message_url)
        return '', 200
    ```

  

* 점심메뉴, 로또

  * ```python
    from flask import Flask, render_template , request
    import requests
    from pprint import pprint
    import random
    
    app=Flask(__name__)
    
    base_url = 'https://api.telegram.org'
    key = '926776064:AAE28UUN9xgJTZ7SXWrmhPbggVyGz8Kk_us'
    update_url = f'{base_url}/bot{key}/getUpdates'
    #message_url = f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}'
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/send')
    def send():
        response = requests.get(update_url).json()
        chat_id = response['result'][0]['message']['chat']['id']
        text= request.args.get('msg')
        message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(message_url)
        return '메시지를 전송하였습니다'
    
    @app.route('/telegram', methods=['POST'])
    def telegram():
        response = request.get_json()
        text = response['message']['text']
        if text == '점심메뉴':
            menu = ['스테이크', '참치회', '장어곰탕', '치킨', '햄버거']
            text = random.choice(menu)
    
        elif text == '로또':
            text = sorted(random.sample(range(1,46),6))
    
            
    
        chat_id = response['message']['chat']['id']
        message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(message_url)
        return '', 200
    
    if __name__=="__main__":
        app.run(debug=True)
    ```

* `<Header>`: 문서에 대한 정보를 말해줌 

* post / request 에서는 parameter 정보를 넘기는 것이 불완전하기 때문에 잘 사용하지 않습니다.



### 네이버 파파고

* 번역

  * ```python
    import requests
    
    client_id = 'Fk5owAIv7c3HmWsMktPm'
    client_secret = 'jvJ1_62im5'
    text = '댕댕이'
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : client_secret,
    }
    
    data = {
        'source' : 'ko',
        'target' : 'en',
        'text' : text,
    }
    
    response = requests.post(papago_url, headers=headers, data=data)
    
    print(response.json())
    ```

    

### 연예인 얼굴인식

* ```python
  import os
  import sys
  import requests
  client_id = "Fk5owAIv7c3HmWsMktPm"
  client_secret = "jvJ1_62im5"
  # url = "https://openapi.naver.com/v1/vision/face" // 얼굴감지
  url = "https://openapi.naver.com/v1/vision/celebrity"
  files = {'image': open('cl.jpg', 'rb')} #rb=readbinary
  headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
  response = requests.post(url,  files=files, headers=headers)
  rescode = response.status_code
  if(rescode==200):
      print (response.text)
  else:
      print("Error Code:" + rescode)
  ```

* #### .env 파일

  * 상수는 무조건 대문자
  * 띄어쓰기는 허용하지 않는다.



### 챗봇 코드

```python
from flask import Flask, render_template , request
import requests
from pprint import pprint
import random
from decouple import config

app=Flask(__name__)
client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

base_url = 'https://api.telegram.org'
key = config('TELEGRAM_BOT_TOKEN')
update_url = f'{base_url}/bot{key}/getUpdates'
#message_url = f'{base_url}/bot{key}/sendMessage?chat_id={i}&text={text}'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    response = requests.get(update_url).json()
    chat_id = response['result'][0]['message']['chat']['id']
    text= request.args.get('msg')
    message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return '메시지를 전송하였습니다'

@app.route('/telegram', methods=['POST'])
def telegram():
    response = request.get_json()
    pprint(response)
    text = response.get('message').get('text')
    
    chat_id = response.get('message').get('chat').get('id')


    if text == '점심메뉴':
        menu = ['스테이크', '참치회', '장어곰탕', '치킨', '햄버거']
        text = random.choice(menu)

    elif text == '로또':
        text = sorted(random.sample(range(1,46),6))

    elif text[0:4]==("/번역 "):
        # 1. papago를 통해 번역을 요청해서 받아오기
        
        papago_url = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {'X-Naver-Client-Id' : client_id,'X-Naver-Client-Secret' : client_secret,}
        data = {'source' : 'ko','target' : 'en','text' : text[4:],}
        papago_response = requests.post(papago_url, headers=headers, data=data)
        
        # 2. 받아온 결과를 telegram 메시지로 보내기
        text=papago_response.json()
        text=text.get('message').get('result').get('translatedText')
        
            

    elif text == 'Hello':
        hello=['안녕', 'Hello', "안녕하세요","Nihao", "Hi", "Ciao"]
        text= random.choice(hello)

    
    message_url = f'{base_url}/bot{key}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return '', 200

if __name__=="__main__":
    app.run(debug=True)
```



TIP

* `data.go.kr`
  * Data Science 분야를 원하는 사람은 사이트 참고!
  * 데이터를 사용하고 싶으면 `활용신청`
  * 일반 인증키 받기 (이것이 열쇠! KEY)
* World Wide Web : Tim-Berners Lee 가 만듦
  * `http://info.cern.ch/hypertext/WWW/TheProject.html`: The first website (WWW)