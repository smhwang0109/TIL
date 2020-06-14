# 0504_Homework

1. Django 는 MTV 로 이루어진 Web Framework 다. MTV 가 무엇의 약자이며 Django 에서 각각 어떤 역할을 하고 있는지 작성하시오.

   Model : 데이터를 표현하는데 사용, 하나의 모델 클래스는 DB에서 하나의 테이블로 표현된다.

   Template : HTML을 생성하는 것을 목적으로 하는 컴포넌트

   View : HTTP Request를 받아 그 결과인 HTTP Response를 리턴하는 컴포넌트. model로부터 데이터를 읽거나 저장할 수 있고 templates를 호출하여 데이터를 UI상에 표현 가능

   

2. 기본적으로 ‘/ ’ 페이지에 접속하게 되면 아래 사진처럼 Page not found 에러가 발생한다. ‘/ ’ 페이지에 접속했을 때 index.html 를 렌더링 하고자 한다. 아래 빈칸에 알맞은코드를 작성하시오. (프로젝트의 이름은 crud 이며 app 이름은 articles 이다. index.html 파일을 렌더링 하는 함수의 이름은 index 라고 가정한다.)

   ![image-20200504175720482](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504175720482.png)

   ![image-20200504175724608](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504175724608.png)

   (a) : articles

   (b) : views

   (c) : views.index

   

3. Django 프로젝트는 기본적으로 render 할 html 과 같은 template 파일과 css , js 와 같은 static 파일을 앱 폴더 내부의 templates 와 static 이름의 폴더에서 찾는다 . 만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 \_\_(a)\_\_파일의 \_\_(b)\_\_과 \_\_(c)\_\_이라는 변수에 담긴 리스트의 요소를 수정하면 된다 . 빈칸 (a), (b), (c) 에 들어갈 내용을 작성하시오.

   (a) : settings.py

   (b) : TEMPLATES

   (c) : DIRS

   

4. 아래는 그림과 같이 Django 에서 선언한 Model 을 Database 에 반영하는 과정에서 사용하는 명령어에 대한 설명이다. 각 설명에 해당하는 명령어를 작성하시오.

   ![image-20200504180018749](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504180018749.png)

   - 마이그레이션 생성

     - python manage.py makemigrations

   - 마이그레이션 DB 반영 여부 확인

     - python manage.py showmigrations

   - 마이그레이션에 대응되는 SQL 문 출력

     - python manage.py sqlmigrate 앱이름 마이그레이션파일번호

   - 마이그레이션 파일의 내용을 DB 에 최종 반영

     - python manage.py migrate

       

5. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - POST 와 GET 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다.

     - F

   - ModelForm 과 Form Class 의 핵심 차이는 Model 의 정보를 알고 있는지의 여부이다.

     - T

   - AuthenticationForm 은 User 모델과 관련된 정보를 이미 알고 있는 ModelForm 으로
     구성되어 있다.

     - F

   - ModelForm 을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다.

     - T

     

6. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 (crud) 내부의 /uploaded_files 로 지정하고자 한다. 이 때 , settings.py 에 작성해야 하는 설정 2 가지를 작성하시오.

   ```python
   MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
   
   MEDIA_URL = '/media/'
   ```

   

7. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - RDBMS 를 조작하기 위해서 SQL 문을 사용한다.

     - T

   - SQL 에서 명령어는 반드시 대문자로 작성해야 동작한다.

     - F

   - 일반적인 SQL 문에서는 세미콜론 ( ; ) 까지를 하나의 명령어로 간주한다.

     - T

   - SQLite 에서 .tables, .headers on 과 같은 dot( . ) 로 시작하는 명령어는 SQL 문이 아니다.

     - F

   - 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다.

     - F

       

8. 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 \__(a)__ 에 들어갈 코드를 작성하시오. 그리고 이러한 설정이 되어있는 상황에서 Article 객체를 삭제하려고 할 때 발생하는 오류를 작성하시오.

   ![image-20200504180820018](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504180820018.png)

   (a) : PROTECT

   오류 : ProtectedError

   

9. Board 모델과 User 모델을 M:N 관계로 설정하여 '좋아요' 기능을 구현하려고 한다. \_\_(a)\_\_ 와 \_\_(b)\_\_ 에 들어갈 내용을 작성하시오. 추가적으로 아래의 상황에서 \_\_(b)\_\_ 를 반드시 작성 해야 하는 이유를 함께 작성하시오.

   ![image-20200504180951813](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504180951813.png)

   (a) : ManyToManyField

   (b) : related_name

   이유 : user와 like_users가 둘 다 User 모델과 관계되어 있기 때문에 User 모델에서 역참조시 board_set으로 이름이 중복되기 때문이다.

   

10. follow 기능을 구현하기 위해 accounts app 의 models.py 에 아래와 같은 모델을 작성하였다. Migration 작업 이후에 Database 에 만들어지는 테이블의 이름을 작성하고 follow 와 관련된 모델의 필드 이름을 각각 작성하시오.

    ![image-20200504181027111](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200504181027111.png)

    테이블 이름 : accounts_user_followers

    필드 이름 : from_user_id, to_user_id