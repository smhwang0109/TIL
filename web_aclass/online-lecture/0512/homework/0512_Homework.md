# 0512_Homework

1. "Javascript 는 \__(a)__ 를 조작할 수 있는 유일한 언어이며 전세계에서 가장 인기 있는 프로그래밍 언어 중 하나 이다 .” \_\_(a)__ 에 들어 갈 말을 작성하시오.

   (a) : 브라우저

   

2. Javascript 에서 변수를 다룰 때 사용하는 키워드는 크게 var, let, const 3 가지가 있다 . 각각의 핵심 특징을 나열하고 block scope 와 function scope 의 차이를 나타내는 예시를 작성하시오.

   - var(function scope) : 변수 재선언 가능

   - let(block scope) : 변수에 재선언 불가능, 재할당 가능

   - const(block scope) : 변수에 재선언 불가능, 재할당 불가능

   - block scope

     ```js
     // 정상 작동
     let c
     c = 'test'
     
     // 에러
     d = 'test'
     let d // ReferenceError: Cannot access 'd' before initialization
     
     // const는 더 엄격
     // 선언과 동시에 값을 할당 해야한다.
     const ee // Missing initializer in const declaration
     ```

     

   - function scope

     ```js
     // 정상 작동
     for(var j=0; j<10; j++) {
         console.log('j', j)
     }
     console.log('after loop j is', j) // after loop j is 10
     
     // 에러
     function counter() {
         for(var i=0; i<10; i++) {
             console.log('i', i)
         }
     }
     counter()
     console.log('after loop i is', i) // ReferenceError: i is not defined
     ```

     

3. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - javascript 에서는 python 의 type() 과 비슷하게 typeof 연산자를 통해서 자료형을 파악할 수 있다.

     - T

   - JSON 은 Javascript Object Notation 의 약자로 Javascript 의 Object 표기법을 따른 문자다.

     - T

   - 화살표 함수는 함수의 선언식 & 표현식과 문법적으로 차이가 있지만 내부 동작은 완전히 동일하기 때문에 무엇을 사용하든 관계없다.

     - T

   - null 과 undefined 는 javascript 의 설계상의 실수이며 typeof 연산자를 통해 확인해보면 모두 undefined 로 나온다.

     - F

       

4. 동등 연산자 와 일치 연산자 의 차이를 간략히 설명하시오.

   - 동등 연산자 ("==", "!=") : 동일한 값이면 같다고 판단
   - 일치 연산자 ("===", "!==") : 동일한 타입, 동일한 값이어야 같다고 판단 