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

// 정상 작동
let c
c = 'test'

// 에러
d = 'test'
let d // ReferenceError: Cannot access 'd' before initialization

// const는 더 엄격
// 선언과 동시에 값을 할당 해야한다.
const ee // Missing initializer in const declaration