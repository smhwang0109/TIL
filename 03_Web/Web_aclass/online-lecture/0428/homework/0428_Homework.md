# 0428_Homework

1. 다음 중 맞으면 T, 틀리면 F를 작성하고 틀렸다면 이유를 함께 작성하시오.

   - Django 에서 1:N 관계는 ForeignKeyField 를 사용하고 M:N 관계는 ManyToManyField를 사용한다.
     - F : ForeignKey를 사용한다.
   - ManyToManyField 를 설정하고 만들어지는 테이블 이름은 앱이름 클래스이름 지정한 필드 이름의 형태로 만들어진다.
     - T
   - ManyToManyField 의 첫번째 인자는 모델 , 두번째 인자는 related_name 이 들어가는데 두 가지 모두 필수적으로 들어가야 한다.
     - F : related_name은 필수가 아니다.

   

2. 빈칸에 들어갈 코드를 작성하시오.

   (a) : request.user

   (b) : article.like_users.all

   

3. 빈칸에 들어갈 코드를 작성하시오.

   (a) : username

   (b) : followers

   (c) : filter

   (d) : remove

   (e) : add

   

4. 에러 메시지가 발생하는 이유와 해결 방법

   이유 : signup 함수에서 장고에서 만들어진 UserCreationForm을 사용하기 때문에 직접 만든 accounts.User 모델이 아니라 auth.User 모델을 사용하기 때문이다.

   해결 방법 : UserCreationForm을 상속한 CustomUserCreationForm을 만들어 accounts.User 모델을 사용하게 만든다.

   

5. 해당 코드에서 related_name을 필수적으로 설정해야 하는 이유

   user와 like_users가 모두 AUTH_USER_MODEL과 관계되어 있기 때문에 related_name을 지정해주지 않으면 역참조 시 'article_set'으로 이름이 겹친다.

   

6. 빈칸에 들어갈 코드를 작성하시오.

   (a) : person.followings.all

   (b) : person.followers.all

   (c) : request.user

   (d) : person

   (e) : person.username

