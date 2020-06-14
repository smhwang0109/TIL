# JavaScript

#### script 태그 : html에게 자바스크립트로 쓴다고 알려주는것

```html
<script>
	document.write(1+1)
</script>
<!--
1+1 이 아니라 2가 출력된다.
-->
```

#### 이벤트 만들기

```html
<body>
    <!--
        on~~~는 이벤트
        그리고 뒤에 오는 것은 자바스크립트 코드
    -->
    <input type="button" value="hi" onclick="alert('hi')">
    <input type="text" onchange="alert('changed')">
    <input type="text" onkeydown="alert('key down!')">
    
</body>
```

#### 콘솔

화면에서 마우스 오른쪽 클릭 해서 '검사' 누르고 'esc'키 누르면 콘솔 창 켤 수 있다.

여기에 코드를 입력하면 자바스크립트로 사용가능하다.

#### 데이터 타입

```javascript
'hello world'.length // 길이
'hello world'.toUpperCase() // 대문자
'hello world'.indexOf('o') // 'o'의 인덱스 위치
'         hello        '.trim() // 공백 제거
```

#### 변수와 대입 연산자

```javascript
var x = 1; // 변수 만들 때는 가급적이면 var 써라
```



