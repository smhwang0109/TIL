# Kotlin 2강 - 변수와 자료형

### 주석

```kotlin
// 주석 처리
/*
멀티라인 주석
*/
```

### 이름 표기법

클래스 이름

- 파스칼 표기법(모든 단어 대문자로 시작)
- ex) ClassName

함수, 변수 이름

- 카멜 표기법(첫 단어만 소문자로 시작)
- ex) functionName



### 변수 선언

#### var

- 일반적으로 통용되는 변수
- 언제든 읽기 쓰기가 가능

#### val

- 선언시에만 초기화 가능
- 중간에 값 변경 불가



### 선언 위치에 따른 변수

#### Property(속성)

- 클래스에서 선언된 변수

#### Local Variable(로컬 변수)

- 클래스 이외의 Scope 내에 선언된 변수



### 변수 선언

```kotlin
fun main() {
    var a: Int = 123
    println(a)
}
// 기본적으로 변수의 기본값인 null을 허용하지 않음

fun main() {
    var a: Int? = null
    println(a)
}
// 이렇게 하면 null 값 허용됨
```



### 자료형

#### 정수형

- Byte : 8bits
- Short : 16bits
- Int : 32bits
- Long : 64bits

```kotlin
fun main() {
    
    var intValue: Int = 1234
    var longValue : Long = 1234L // L을 붙여서 더 큰 변수임을 표시
    var intValueByHex : Int = 0x1af // 0x 붙여서 16진수
    var intValueByBin : Int = 0b10110110 // 0b를 분여서 2진수
    
}
```



#### 실수형

- Float : 32bits
- Double : 64bits

```kotlin
fun main() {
    
    var doubleValue:Double = 123.5
    var doubleValueWithExp:Double = 123.5e10
    var floatValue:Float = 123.5f
    
}
```

#### 문자형

- Char : 1개의 문자
- 유니코드 UTF-16BE 방식
  - 글자 하나가 2Byte(16bit)의 메모리 공간을 사용한다.

```kotlin
fun main() {
    
    var charValue:Char = 'a'
    var koreanCharValue:Char = '가'
    
}
```

- 특수문자 지원

![image-20200307133158403](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20200307133158403.png)

#### 문자열

```kotlin
fun main() {
    
    val stringValue = "one line string test"
    
    val multilineStringValue = """multiline
    string
    test"""
    
}
```



#### 논리형

- Boolean : 참 또는 거짓

```kotlin
fun main() {
    
    var booleanValue:Boolean = True
    
}
```





***Tip!**

warning : 치명적이지는 않지만 불필요한 구문이 있거나 잠재적 문제가 있을 수 있음

error : 구문상에 심각한 문제가 생겨 컴파일 자체가 불가능한 상태