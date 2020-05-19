// class 없이 객체 만들기
const unani92 = {
    name: '정윤환',
    birth: '1992',
    greeting: function() {
        return '안녕하십니까'
    },
    'greeting': function() {
        return '안녕하십니까'
    },
    greeting() {
        return '안녕하십니까'
    },
    greeting() {
        return `안녕하십니까 ${this.name}입니다.`
    }
}

console.log(unani92['name'])
console.log(unani92.name)
console.log(unani92.greeting())
unani92.money = 5000
console.log(unani92.money)

// class로 객체 만들기
class Person {
    constructor(name, birth) {
        this.name = name
        this.birth = birth
    }
    greeting() {
        return `안녕하십니까. ${this.name}입니다.`
    }
}

const unani = new Person('정윤환', 1992)
const hangrae = new Person('조항래', 1992)

console.log(unani.name)
console.log(unani.greeting())

console.log(hangrae.name)
console.log(hangrae.greeting())

const a = null
const b = undefined

console.log(typeof(a))
console.log(typeof(b))
