# Heroku 배포

1. 기본 헤로쿠 배포

https://egg-money.tistory.com/115

2. 강동주 강사님 헤로쿠 배포

https://lab.ssafy.com/john/heroku_deploy

3. 헤로쿠 + 클라우디너리 (미디어 추가 시)

https://www.dothedev.com/blog/heroku-django-store-your-uploaded-media-files-for-free/



### git push heroku master 시 오류 해결 방법

1. 오타 확인 (Procfile, runtime 등)
2. static file 오류 시 heroku config:set DISABLE_COLLECTSTATIC=1 입력



### Heroku에 .env 보내기

`.env` 파일에 있는 사항을 heroku로 보낼 수 있는 방법을 찾다 `heroku-dotenv` package를 찾게 되었습니다. 사용 방법은 아래와 같습니다.

```powershell
$ npm i -g heroku-dotenv
$ heroku-dotenv push
```

이렇게 하면 `heroku-dotenv` 가 제가 `.env` 파일에 저장해 놓은 환경변수들을 연결되어 있는 heroku서버에 전달하고 적용시킵니다.



### Heroku error 1

![Heroku error 1](C:\Users\user\house\TIL\배포\Heroku error 1.JPG)

1. Procfile 확인
2. 코드 오타 확인(heroku run python manage.py migrate 로 확인 가능)

#### 참고

https://dev.to/lawrence_eagles/causes-of-heroku-h10-app-crashed-error-and-how-to-solve-them-3jnl







### 참고

[https://ggilrong.tistory.com/entry/heroku%EC%97%90-django-%EC%95%B1%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0](https://ggilrong.tistory.com/entry/heroku에-django-앱배포하기)