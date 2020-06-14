# 0511_Homework

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - URL 는 정보의 자원 뿐만 아니라 HTTP Method 를 통해 무엇을 어떻게 하고 싶은지 명확하게 나타내야 한다.

     - T

   - 자원에 대한 행위는 HTTP Method 로 표현한다.

     - T

   - 일반적으로 주소 마지막에 슬래시 ( / )는 포함하지 않는다.

     - T

   - https ://www.fifa.com/worldcup/teams/team/43822/create 는 계층 관계를 잘 표현한 RESTful 한 URI 라고 할 수 있다.

     - F

     

2. 다음의 HTTP status code 의 의미를 간략하게 작성하시오.

   - 200(성공) : 서버가 요청을 제대로 처리했다.

   - 400(잘못된 요청) : 서버가 요청의 구문을 인식하지 못했다.

   - 401(권한 없음) : 인증이 필요한 요청에 권한이 없는 상태로 요청을 했다. (인증 실패)

   - 403(Forbidden, 금지됨) : 서버가 요청을 거부하고 있다. 필요한 권한이 없다. (인가 실패)

   - 404(Not Found, 찾을 수 없음) : 서버가 요청한 페이지를 찾을 수 없다.

   - 500(내부 서버 오류) : 서버에 오류가 발생하여 요청을 수행할 수 없다.

     

3. DRF 를 활용하여 학생 정보를 제공하는 API 를 제작하고자 한다 . 학생 모델은 models.py 에 아래와 같이 정의되어 있고 , 학생 모델의 데이터를 다른 유형의 데이터 포맷으로 변환할 수 있는 Serializer 를 정의하려고 한다 . Serializers.py 파일에 들어갈 StudentSerializer 를 정의하시오 . 단 , name 과 address 필드는 반드시 포함되어야 한다.

   ![image-20200511183820356](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200511183820356.png)

   ```python
   from rest_framework import serializers
   from .models import Student
   
   class StudentSerializer(serializers.ModelSerializer):
       class Meta:
           model = Student
           fields = '__all__'
   ```

   

