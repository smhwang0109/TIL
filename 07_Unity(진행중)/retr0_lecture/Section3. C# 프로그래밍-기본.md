# Section3. C# 프로그래밍-기본

## 1. 변수와 함수의 이해

### 변수

> 값(Value)이 할당되는 이름

- 변수에 할당된 데이터는 런타임(게임 도중)에 얼마든지 접근하여 수정 가능

```C#
int gold = 200;
float itemWeight = 1.3f;
bool itemUsed = true;
string itemName = "Potion";
```



### 함수

> 미리 정해진 동작을 수행하는 코드 묶음

```C#
void Attak(Monster target, int damage, int point) {
    PlayAnimation();
    PlaySound();
    target.hp = target.hp - damage;
    exp = exp + point;
}

Monster ork
Attack(ork, 5, 30);
    
Monster goblin
Attack(goblin, 20, 5);

int GetRandomNumber() {
    int number = 0;
    number = 랜덤한 숫자
    return number
}

fuctionType FunctionName(variableType inputName) {

}
```

- fuctionType
  - void : return 값이 없다.
  - int, float, string, bool 등등 : return type



## 2. 콘솔 출력 + C# 기본 변수

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloUnity : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
        Debug.Log("Hello World");

        int age = 23;
        int money = -1000;

        Debug.Log(age);
        Debug.Log(money);

        // floating point - float: 소숫점을 가지는 실수: 32비트
        // 소숫점 아래 7자리까지만 정확(그 이상은 근사값 처리)
        float height = 169.1234567f;

        // float의 두배의 메모리를 사용: 64비트
        // 소숫점 아래 15자리까지만 정확
        // 정확한 것은 성능이 않좋다는 것이기 때문에 게임에서는 float을 사용
        double pi = 3.14159265359;

        bool isBoy = true;
        bool isGirl = false;

        // char : character 는 한 문자 
        char grade = 'A';

        // string : 문장
        string movieTitle = "라이브!";

        Debug.Log("내 나이는!: " + age);

        Debug.Log("내가 가진 돈은!: " + money);

        // var는 할당하는 값을 기준으로 타입을 결정
        var myName = "Soom";
        var myAge = 23;
        var pi2 = 3.141592f;


    }
}
```



## 3. 사칙 연산 + 복합 연산자

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloMath : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        int i = 0;

        Debug.Log(i++); // 0
        
        Debug.Log(i); // 1

        Debug.Log(++i); // 2

        Debug.Log(i); // 2

        int j = 10;

        j += 5; // j = j + 5
        
        j -= 5; // j = j - 5

    }
}
```



## 4. 함수 + 스코프

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloFunction : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        float sizeOfCicle = 30f;

        float radius = GetRadius(sizeOfCicle); // 전역 변수

        Debug.Log("원의 사이즈 : " + sizeOfCicle + " 원의 반지름 : " + radius);
    }

    float GetRadius(float size) {
        float pi = 3.14f;

        float tmp = size/pi;

        float radius = Mathf.Sqrt(tmp); // 지역 변수

        return radius;
    }

}
```



## 5. 형변환 + 조건문

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloCSharp : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
        // 형변환(Casting)
        int height = 170;
        float heightDetail = 170.3f;

        // 자동 형변환 (잃어버리는 정보가 없으면)
        heightDetail = height;

        // 직접 명시해야 하는 경우
        height = (int)heightDetail;

        Debug.Log(height);
        Debug.Log(heightDetail);

        // 조건문 if문
        bool isBoy = true;

        if(isBoy == true) {
            Debug.Log("나는 남자다.");
        }
        else {
            Debug.Log("나는 여자다.");
        }

        int age = 18;

        // || : or 
        if (age >= 60 || age <= 5) {
            Debug.Log("노약자입니다.");
        }

        // && : and
        if (age < 60 && age > 5) {
            Debug.Log("노약자가 아닙니다.");
        }

        // ! : not
        if (!isBoy) {
            Debug.Log("나는 여자다.");
        }
        Debug.Log("! true = " + !true);

    }
}
```



## 6. 분기문 + 반복문

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloCSharp : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

        // Switch 분기문
        int year = 2017;

        switch(year) {
            case 2012:
                Debug.Log("레미제라블");
                break;
            case 2016:
                Debug.Log("곡성");
                break;
            case 2017:
                Debug.Log("트랜스포머5");
                break;
            default:
                Debug.Log("연도가 해당사항 없음");
                break;
        }

        // 루프문 Loop 반복문들

        // for 문
        // 초기화; 조건; 업데이트
        for(int i = 0; i < 10; ++i) {
            Debug.Log("현재 순번: " + i);
        }
        Debug.Log("루프 끝");

        // while 문
        bool isShot = false;
        int index = 0;
        int luckyNumber = 7;
        while (isShot == false) {
            index += 1;
            if (index == luckyNumber) {
                Debug.Log("총알에 맞았다.");
                isShot = true;
            }
            else
            {
                Debug.Log("총알에 맞지 않았다.");
            }
        }

        // do-while 문 : while 문 조건 가기 전에 한번은 실행하고 한다.
        do {
            Debug.Log("Do-While");
            Debug.Log("여기에 반복할 코드를 입력");
        } while(isShot == false);

    }
}
```



## 7. 배열

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloArray : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // 배열 : 여러개의 값을 하나의 변수로 다루게 해준다.
        int[] scores = new int[10];
        scores[0] = 90;
        scores[1] = 45;
        scores[2] = 60;

        Debug.Log(scores[0]); // 90
        Debug.Log(scores[3]); // 0
        scores = new int[20];
        Debug.Log(scores[0]); // 0
    }

}
```



## 8. 클래스와 오브젝트

```c#
// HelloClass

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Animal {

    public string name;
    public string sound;
    public float weight;

}
public class HelloClass : MonoBehaviour
{
    void Start() {
        Animal jack = new Animal();
        jack.name = "JACK";
        jack.sound = "Bark";
        jack.weight = 4.5f;

        Animal nate = new Animal();
        nate.name = "NATE";
        nate.sound = "Nyaa";
        nate.weight = 1.2f;

        Animal annie = new Animal();
        annie.name = "ANNIE";
        annie.sound = "Wee";
        annie.weight = 0.8f;

        nate = jack;

        nate.name = "JIMMY";
        nate.sound = "Cheeze";

        Debug.Log(jack.name);
        Debug.Log(jack.sound);
        
        Debug.Log(nate.name);
        Debug.Log(nate.sound);
        
        Debug.Log(annie.name);
        Debug.Log(annie.sound);        
    }
}
```

```c#
// Jumper

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jumper : MonoBehaviour
{
    public Rigidbody rb; // Rigidbody를 가져와서 사용한다.
    void Start()
    {
        rb.AddForce(0, 1000, 0);
    }
}

```

