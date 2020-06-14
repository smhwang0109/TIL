# HTML(HyperText Markup Language) Grammer

### 닫는 태그가 있는 것

#### head와 body 감싸기

```html
<!doctype html>
<html>
    <head>
        
    </head>
    <body>
        
    </body>
</html>
```



#### 본문 파트(body)

```html
# body 묶기
<body>

# 굵은 글씨
<strong></strong> 

# underline
<u></u> 

# 단락(paragraph)
<p>
</p>

# p 태그는 한칸을 꼭 띄는 단점 있음
# 이를 극복하기 위해 CSS 사용
# 위쪽에 45px만큼 여백 생성
<p style="margin-top:45px;">
</p>

# 서로 부목 자식 관계로 꼭 필요한 태그
# 목차(list)
# 순서가 없는 경계(unordered list)
# 순서가 있는 경계(ordered list)
<ul>
    <li>1. HTML</li>
	<li>2. CSS</li>
	<li>3. JavaScript</li>
</ul>
<ol> # 숫자를 안써줘도 자동으로 작성해줌
    <li>HTML</li>
	<li>CSS</li>
	<li>JavaScript</li>
</ol>

# 링크 걸기
# a == anchor(닻)
# href == HyperText Reference
# target="_blank" : 링크 클릭했을 때 새창에서 페이지 열기
# title : 이 링크가 담고 있는 내용 (툴팁)
    
<a href="https://www.w3.org/TR/html5/" target="_blank" title="html5 specification">Hypertext Markup Language (HTML)</a>
    
# HTML 주석처리
<!--
여기는 주석처리된 구간입니다.
-->
    
    
    
</body>
```

#### 본문 설명 파트(head)

```html
# head 묶기
<head>
# 제목 지정 태그
<title> HTML-공부하기 </title>
<meta charset="utf-8"> # 한글이 깨지지 않게 utf-8 형식으로 해석하라는 뜻

</head>
```



### 닫는 태그 없는 것

```html
# 새로운 줄 표현
# 하지만 사실상 <p></p> 태그를 더 많이 사용
<br><br> 
# 하나 입력할때마다 한 번 Enter한 기능
# 두개 입력했으니까 두 번 Enter한 것

# 이미지 삽입
# src = sorce
<img src="https://s3-ap-northeast-2.amazonaws.com/opentutorials-user-file/module/3135/7648.png" width="100%">
```





## 웹 서버 만들기

Apache를 다운 받아야 하지만 어려우므로

bitnami를 이용해 쉽게 Apache를 다운받을 수 있다.

다운받는 법 : https://opentutorials.org/course/3084/18893

다운 링크 : https://bitnami.com/stack/wamp



- 다 같은 주소
  - Domain 주소 : http://localhost/index.html
  - IP(Internet Protocol) 주소 : http://127.0.0.1/index.html
  - 내 IP 주소 : http://19x.xxx.x.xx/index.html
- 매니저 열기
  - C:\Bitnami\wampstack-7.3.13-0
  - 여기의 manager-windows 실행

- index.html 위치
  - C:\Bitnami\wampstack-7.3.13-0\apache2\htdocs
  - 해당위치에 폴더 다 지우고 내가 열 파일들 다 넣으면 IP주소로 열린다.
- http:// : HyperText Transfer Protocol (웹페이지를 전송하기 위해서 만든 통신 규약)