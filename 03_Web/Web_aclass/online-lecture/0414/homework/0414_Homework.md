# 0414_Homework

1. User 모델에서 사용할 수 있는 컬럼 중 BooleanField로 정의 된 컬럼

   is_staff, is_active

   

2. User 모델의 username에 저장할 수 있는 최대 길이

   150 글자

   

3. 코드 작성

   (a) : AuthenticationForm

   (b) : login

   (c) : form.get_user()

   

4. 로그인 확인을 위해 정의된 속성 이름

   is_authenticated

   

5. 로그인 하지 않았을 경울 template에서 user 변수 출력하면 나오는 클래스 이름

   AnonymousUser

   

6. django의 User모델 암호화를 위해 사용되는 알고리즘 이름

   SHA(Secure Hash Algorithm)

   

7. 로그아웃 실행 시 문제 발생 원인과 해결 방법

   원인 :

   1. django.contrib.auth의 logout 과 새로 정의하는 함수 logout이 이름이 같기 때문입니다.
2. 오류는 안나지만 login 하지 않은 경우도 url을 통해 logout에 접근이 가능하다.
   
   해결 방법 :
   
   1. import 할 때 별명을 설정한다.
   2. login_required 데코레이터를 이용한다.
   
   ```python
from django.contrib.auth import logout as auth_logout
   from django.contrib.auth.decorators import login_required

   @login_required
   def logout(request):
       auth_logout(request)
       return redirect('accounts:login')
   ```
   
   
   
   

