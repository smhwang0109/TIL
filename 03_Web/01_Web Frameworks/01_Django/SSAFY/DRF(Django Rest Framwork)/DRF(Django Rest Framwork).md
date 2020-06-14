# DRF(Django Rest Framwork)

### load/dump data (* c9/practice/0511/workshop/api 참고)

![load_dump_data](C:\Users\user\house\TIL\Django\DRF(Django Rest Framwork)\load_dump_data.JPG)

1. 프로젝트폴더/앱폴더/fixtures 폴더 생성
2. fixtures 폴더에 json 파일 넣기
3. load data 하기

```shell
python manage.py loaddata dummy.json

python manage.py dumpdata 앱이름(.모델이름)
python manage.py dumpdata musics --indent 2 > dump.json
```

