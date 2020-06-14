# JavaScript

## 출력

```js
consol.log("Hello World!")
consol.log(`Hello ${name} you are ${age} years old!`)
// 객체(object)에서 쓸 수 있는 속성(property)를 보여주는 property
consol.dir()
```

## 변수

- let
  - 변할 수 있는 변수
- const
  - 변할 수 없는 변수

## 주석

- //
- /**/

## 배열

```javascript
const A = [1,2,3]
```

## 객체

```javascript
const soomInfo = {name:"Soom", age:26, gender:"Male", isHandsome:true}
```

## BOM

자바스크립트의 document로 htm과 CSS를 조작하는것

```js
const title = document.getElementById("title");
// CSS처럼 자식에 있는 선택자를 찾아줌 class는 . , id 는 #
const title = document.querySelector("#title");
```

## if else

```js
if (20 > 5 && "nicolas" === "nicolas") {
    console.log("yes");
} else {
    console.log("no");
}
```

## classlist

class에 무언가가 들어있을 때 추가하고 제거하는 등의 조작을 할 수 있다.

```js
const title = document.querySelector("#title");

const CLICKED_CLASS = "clicked";

function handleclick() {
    const hasClass = title.classList.contains(CLICKED_CLASS);
    if (hasClass) {
        title.classList.remove(CLICKED_CLASS);
    } else {
        title.classList.add(CLICKED_CLASS);
    }
}
/* 같은 것
function handleclick() {
    title.classList.toggle(CLICKED_CLASS);
}
*/

function init() {
    title.addEventListener("click", handleclick);
}
init();
```

