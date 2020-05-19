// 1. 선언식(사용 안한다.)
function add(num1, num2) {
    return num1 + num2
}

add(1, 2)

// 파이썬
// def add(num1, num2):
// add(1, 2)

// 2. 표현식
const sub = function(num1, num2) {
    return num1 - num2
}

// sub = lambda 입력값: 출력값

// 3. Arrow Function
const arrow = function(name) {
    return `hello! ${name}`
}

const arrow = (name) => {
    return `hello! ${name}`
}

const arrow = name => {
    return `hello! ${name}`
}

const arrow = name => `hello! ${name}`
// arrow function 축약형 사용 가능 조건
// (1) 인자 1개
// (2) return 있어야 하고
// (3) return expression이 1줄이어야 한다.