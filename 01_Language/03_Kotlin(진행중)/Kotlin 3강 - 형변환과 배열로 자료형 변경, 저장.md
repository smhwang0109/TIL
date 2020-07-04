# Kotlin 3강 - 형변환과 배열로 자료형 변경, 저장

### 형변환

**종류**

- toByte()
- toShort()
- toInt()
- toLong()
- toFloat()
- toDouble()
- toChar()



**명시적 형변환**

- 변환될 자료형을 개발자가 직접 지정함

```kotlin
fun main() {
    
    var a: Int = 54321
    var b: Long = a.toLong()
  
}
```

\* Kotlin은 암시적 형변환을 제공하지 않음





### 배열

```kotlin
fun main() {
    
    var intArr = arrayOf(1, 2, 3, 4, 5)
    
    var nullArr = arrayOfNulls<Int>(5) // <> 안에는 자료형이 들어가면 됨 (Generic)
    
    intArr[2] = 8
    
    println(intArr[4])
    
}
```

처음 선언했을 때의 전체 크기를 변경할 수 없다는 단점

한 번 선언해두면 다른 자료구조보다 빠른 입출력이 가능하다는 장점