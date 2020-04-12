# 0330_homework

## Django Template Language

1. menus 리스트를 반복문으로 출력하시오.

   (a) : menu

2. post 리스트를 반복문을 활용하여 0번 글부터 출력하시오.

   (a) : forloop.counter0

3. user 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

   (a) : empty

4. 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

   (a) : if 

   (b) : else

5. 출력된 결과가 주석과 같아지도록 하시오.

   (a) : |length

   (b) : |title

6. 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

   (a) : Y년 m월 d일 (D) A h i





## form tag

1. 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.

   정답 : form을 제출하고 보내지는 url입니다.

2. 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.

   GET, POST

3. input 태그에 각각 '안녕하세요', '반갑습니다', '파이팅' 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.

   정닶 : /create/?title=안녕하세요&content=반갑습니다

