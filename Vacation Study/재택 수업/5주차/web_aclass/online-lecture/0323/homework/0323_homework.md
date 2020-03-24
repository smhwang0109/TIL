# 0323_homework.md

1. Flex box의 주축을 변경하는 flex-direction의 네가지 값과 각각의 특징을 작성하시오.

   row : 행을 기준으로 왼쪽에서 오른쪽 방향으로 주축 변경 (기본값)

   row-reverse : 행을 기준으로 오른쪽에서 왼쪽 방향으로 주축 변경

   column : 열을 기준으로 위에서 아래 방향으로 주축 변경

   column-reverse : 열을 기준으로 아래에서 위 방향으로 주축 변경

   

2. flex-direction의 네가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

   flex-row, flex-row-reverse, flex-column flex-column-reverse

   

3. align-items 속성의 네가지 값과 각각의 특징을 작성하시오.

   stretch : cross 축 전체를 채운다. (기본값)

   flex-start, flex-end : cross 축의 시작위치 혹은 끝 위치로 정렬

   center : cross 축의 가운데로 정렬

   baseline : 문자의 baseline으로 정렬

   

4. flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.

   정답 : (1)  flex-direction, flex-wrap

   

5. 그림과 같은 마크업을 하기 위해 빈칸에 들어갈 클래스를 작성하시오.

   border border-danger

   

6. 두 요소의 차이점을 작성하시오.

   ```html
   <div class="d-flex justify-content-between"></div>
   <!-- 내부 요소들이 div의 끝에서 끝으로 같은 space를 가지고 채운다.
   	 div 양 끝 내부에 space가 없다.-->
   
   <div class="d-flex justify-content-around"></div>
   <!-- 내부 요소들이 본인 양옆에 같은 space를 가지고 채운다.
   	 dic 양 끝 내부에 space가 있다.-->
   ```

   

7. 두 요소의 차이점을 작성하시오.

   ```html
   <div class="fixed-bottom"></div>
   <!-- 아래쪽에 고정된다. body와 영역이 겹친다. -->
   
   <div class="sticky-top"></div>
   <!-- 위쪽에 고정된다. body와 영역이 겹치지 않는다. -->
   ```

   

8. 부트스트랩에서 색상을 표현하기 위한 클래스 중 빨강색을 표현하는 것을 고르시오.

   정답 : (3) danger