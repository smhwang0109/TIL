# CSS Grammer

CSS는 기본적으로 HTML에서 사용하지만

CSS를 사용한다는 것을 웹브라우저에 알려주기 위해 head 태그 안에 style 태그를 넣어서 CSS문법으로 사용가능하다.

```html
<head>
    # CSS 문법이다.
    <style>
        # a tag의 색깔을 검정색으로 바꿔라
        # a {}는 선택자(selector)
        # color:black; 는 효과(declaration)
        # color는 속성(property)
        # black은 값(value)
        a {
            color:black;
            text-decoration: none; # 링크에 나타나는 밑줄 없애기
        }
        
        h1 {
            font-size:60px;
            text-align:center;
        }
    </style>
</head>
```

또는 CSS가 아닌 HTML의 속성(style 속성)으로 CSS를 불러와 사용 가능하다.

이 때 값으로는 CSS의 효과가 들어온다.

이러면 CSS 리스트가 클릭되었을 때만 빨간색에 밑줄로 바뀐다.

```html
<li><a href="2.html" style="color:red;text-decoration:underline">CSS</a></li>
```



### 선택자 다루기

```html
<!doctype html>
<html>
<head>
  <title>WEB - CSS</title>
  <meta charset="utf-8">
  <style>
    a {
      color:black;
      text-decoration: none;
    }
    # 같은 calss 선택자끼리는 호출위치와 가까운 것이 더 우선이지만
    # class와 id 선택자 중에서는 id 선택자가 먼저이다.
    # id 선택자는 한 문서에서 딱 한번만 나와야 한다.
    # saw class 선택자
    .saw {
       color:gray;
      }
    # actice id 선택자
      #active {
          color:red;
      }
    h1 {
      font-size:45px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
      # saw라는 클래스를 만들어서 한번 본 링크들을 묶어 그룹으로 만든다.
      # active라는 id를 만들어서 묶는다.
    <li><a href="1.html" class="saw ac">HTML</a></li>
    <li><a href="2.html" class="saw" id="active">CSS</a></li>
    <li><a href="3.html">JavaScript</a></li>
  </ol>
  <h2>CSS</h2>
  <p>
    Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications.
  </p>
  </body>
  </html>
```

호출 순서

강함 -----------------------------------------약함

id 선택자 -> class 선택자 -> 태그 선택자



### 박스 모델

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        /*
        CSS의 주석
        */
        /*
        block level element(tag) : 한 줄 전체를 차지하는 태그
        */
        h1{
            border-width:5px;
            border-color:red;
            border-style: solid;
            display: inline;/*inline 태그처럼 사용*/
            /*
            display: none; 하면 안보이게도 가능
            */
        }
        /*
        inline element(tag) : 필요한 만큼만 차지하는 태그
        */
        a{
            border-width:5px;
            border-color:red;
            border-style: solid;
            display: block;/*block 태그처럼 사용*/
        }
        /* 
        이렇게도 사용 가능
        */
        h1, a{
            border:5px solid red;
        }
        

    </style>
</head>
<body>
    <h1>CSS</h1>
    Cascading Style Sheets (<a href="https://www.google.com/search?q=css&oq=css"> CSS </a>) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications.
    
</body>
</html>
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        /*
        페이지에서 검사 눌러서 보면 어떤 기능들인지 볼 수 있다.
        border : 테두리
        padding : 문자와 테두리 사이 여백
        margin : 테두리 바깥 여백
        width : block 넓이
        */
        h1{
            border:5px solid red;
            padding: 20px;
            margin:20px;
            display: block;
            width: 100px;
        }
    </style>
</head>
<body>
    <h1>CSS</h1>
    <h1>CSS</h1>
</body>
</html>
```



박스모델로 꾸미기

```html
<!doctype html>
<html>
<head>
  <title>WEB - CSS</title>
  <meta charset="utf-8">
  <style>
    body {
        margin:0;
    }
    #active {
      color:red;
    }
    .saw {
      color:gray;
    }
    a {
      color:black;
      text-decoration: none;
    }
    h1 {
      font-size:45px;
      text-align: center;
      border-bottom:1px solid gray;
      margin:0;
      padding: 20px;
    }
    ol {
        border-right:1px solid gray;
        margin: 0;
        width: 100px;
    }
  </style>
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
  <ol>
    <li><a href="1.html" class="saw">HTML</a></li>
    <li><a href="2.html" class="saw" id="active">CSS</a></li>
    <li><a href="3.html">JavaScript</a></li>
  </ol>
  <h2>CSS</h2>
  <p>
    Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language.[1] Although most often used to set the visual style of web pages and user interfaces written in HTML and XHTML, the language can be applied to any XML document, including plain XML, SVG and XUL, and is applicable to rendering in speech, or on other media. Along with HTML and JavaScript, CSS is a cornerstone technology used by most websites to create visually engaging webpages, user interfaces for web applications, and user interfaces for many mobile applications.
  </p>
  </body>
  </html>
```



### 그리드

[caniuse 홈페이지](http://caniuse.com/)

CSS, HTML, JavaScript의 기술들이 각각의 브라우저 몇버전에서 사용 가능한지 알려주는 사이트



```	html

```

