# Section5. C# 프로그래밍-중급1

## 1. 벡터 연산 기초

- 벡터는 길이와 방향을 가진다.
- 절대 좌표
  - 현재 위치는 (3, 3)
- 상대 좌표
  - 내 위치에서부터 (3, 3)

 

## 2. 평행이동과 좌표계 + 부모 자식 관계

```C#
// Hello Vector/Mover.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mover : MonoBehaviour
{
    public Vector3 move = new Vector3(-5,5,-5);
    void Start()
    {
        // Object의 transform 속성과 연결
        // transform.Translate(move);
        // transform.position += move; 같은 뜻
        // transform.position = new Vector3(0,0,0); global position
        transform.localPosition = new Vector3(0,0,0); // local position

        // transform.rotation;
        // transform.localRotation;
        // transform.lossyScale;
        // transform.localScale;

    }

    void Update()
    {
        if (Input.GetKey(KeyCode.Space))
        {
            Move();
        }
    }

    void Move()
    {
        // Space.World : Global Space를 기준으로 이동
        // Space.Self : Local Space를 기준으로 이동
        transform.Translate(move * Time.deltaTime, Space.World);
    }
}

```



## 3. 회전과 쿼터니언

```c#
// Hello Vector/SetRotation.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SetRotation : MonoBehaviour
{
    public Transform targetTransform;
    void Start()
    {
        // 쿼터니언(x,y,z,w)
        // Unity에서 Vector를 이용하여 Quaternion을 사용할 수 있도록 만들어놨다.
        // Quaternion 사용이유 
        // 기본적으로 x,y,z 축을 기준으로 한 축씩 움직이기 때문에
        // 한 축을 기준으로 90도를 회전하면 
        // 나머지 두 개의 축 중 하나의 움직이기 전과 다른 하나의 움직인 후의 방향이
        // 같은 방향을 가리키기 때문에 다른 축으로 판별이 어려워져
        // 축이 겹쳐서 같이 움직이게 된다.
        // 이를 방지하기 위해 Quarternion을 사용한다.

        // Quaternion newRotation = Quaternion.Euler(new Vector3(30,45,60));
        // transform.rotation = newRotation;

        // Vector3 direction = targetTransform.position - transform.position;
        // Quaternion targetRotation = Quaternion.LookRotation(direction); // 해당 물체를 바라보도록(Z축이 정면)
        // transform.rotation = targetRotation;

        // Quaternion aRotation = Quaternion.Euler(new Vector3(30, 0, 0));
        // Quaternion bRotation = Quaternion.Euler(new Vector3(60, 0, 0));
        // Quaternion targetRotation = Quaternion.Lerp(aRotation, bRotation, 0.5f); // 두 값의 중간 값
        // transform.rotation = targetRotation;

        // transform.Rotate(new Vector3(30, 0, 0)); // 현재 위치에서 30도 더 회전

        // Quaternion originalRotation = transform.rotation; // 현재 Object의 rotation 값 Quaternion으로 가져오기
        // Debug.Log(originalRotation);
        // Vector3 originalRotationInVector3 = originalRotation.eulerAngles; // Quaternion 값 Vector 값으로 변경
        // Debug.Log(originalRotationInVector3);
        // Vector3 targetRotationVec = originalRotationInVector3 + new Vector3(30,0,0);
        // Quaternion targetRotation = Quaternion.Euler(targetRotationVec);
        // transform.rotation = targetRotation;

        // Quaternion originalRotation = Quaternion.Euler(new Vector3(45, 0, 0));
        // Quaternion plusRotation = Quaternion.Euler(new Vector3(30, 0, 0));
        // Quaternion targetRotation = plusRotation * originalRotation;
        // transform.rotation = targetRotation;

        transform.Rotate(new Vector3(30, 0, 0)); // 로컬 기준 30도 회전

    }
}
```



## 4. 인스턴스화

> 특정 Object를 계속 만들어 낼 수 있도록 하는 것

```c#
// Hello Vector/Spawner.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    public Transform spawnPosition;
    public GameObject target;
    // public Rigidbody target;
    void Start()
    {
        GameObject instance = Instantiate(target, spawnPosition.position, spawnPosition.rotation);
        // Rigidbody instance = Instantiate(target, spawnPosition.position, spawnPosition.rotation);

        instance.GetComponent<Rigidbody>().AddForce(0, 1000, 0);
        // instance.AddForce(0, 1000, 0);

        Debug.Log(instance.name);
    }
}

```



## 5. 오버로드

> 함수의 여러가지 버젼을 만드는 것
>
> 하나의 함수 이름에 입력이나 출력을 다르게 해 생성 가능

```C#
// Hello Vector/Calc.cs

public class Calc : MonoBehaviour
{
    void Start()
    {
        Debug.Log(Sum(1, 1));
        Debug.Log(Sum(-5, 8, 10));
        Debug.Log(Sum(1.3f, 1.6f));
    }

    public int Sum(int a, int b)
    {
        return a + b;
    }
    
    public int Sum(int a, int b, int c)
    {
        return a + b + c;
    }

    public float Sum(float a, float b)
    {
        return a + b;
    }
}

```



## 6. 정적 변수와 정적 함수

> 모든 함수들이 공유하는 단 하나의 변수

```C#
// Hello Vector/Dog.cs

public class Dog : MonoBehaviour
{
    public string nickName;

    public float weight;

    public static int count = 0;

    void Awake()
    {
        count += 1;
    }

    void Start()
    {
        Bark();
    }

    public void Bark()
    {
        Debug.Log("모든 개들의 수 : " + count);
        Debug.Log(nickName + ": Bark!");
    }

    public static void ShowAnimalType()
    {
        Debug.Log("개입니다.");
    }

}

```



## 7. 리스트

> 크기를 정하지 않고 들어오는만큼 크기가 조절된다.

```C#
// Hello Vector/ScoreManager.cs

using System.Collections;
using System.Collections.Generic; // 이게 있어야 List 사용 가능
using UnityEngine;

public class ScoreManager : MonoBehaviour
{
    public List<int> scores = new List<int>();
    // public int[] scores = new int[10];

    // private int index = 0;


    void Update()
    {
        if (Input.GetMouseButtonDown(0)) // 마우스 왼쪽 버튼
        {
            int randomNumber = Random.Range(0, 100);
            scores.Add(randomNumber); // 인덱스를 지정할 필요 없이 공간을 하나 늘리고 값을 넣는다.
            // scores[index] = Random.Range(0, 100);
            // index++;
        }

        if (Input.GetMouseButtonDown(1)) // 마우스 오른쪽 버튼
        {
            scores.RemoveAt(3); // 리스트는 해당 인덱스 값이 없어지면 이후 인덱스 들이 하나씩 줄어든다.
        }
    }
}
```



## 8. 싱글톤

> 메모리 상에 단 하나만 존재하며 언제 어디서든 접근 가능한 Object를 만들 때 사용하는 디자인 패턴

### 8-1. 싱글톤 아이디어

```C#
// Hello Vector/Ninja.cs

public class Ninja : MonoBehaviour
{
    public static Ninja ninjaKing;
    public string ninjaName;

    public bool isKing;

    void Start()
    {
        if(isKing)
        {
            ninjaKing = this; // this == 자기 자신을 가리키는 키워드
        }
    }

    void Update()
    {
        Debug.Log("My Name: " + ninjaName + ", Ninja King is" + ninjaKing);
    }
}

```



### 8-2. 싱글톤 만들기

```C#
// Singleton/ScoreManager.cs

public class ScoreAdder : MonoBehaviour
{
    // public ScoreManager scoreManager;

    void Update() 
    {
        if(Input.GetMouseButtonDown(0))
        {
            ScoreManager.GetInstance().AddScore(5);
            // scoreManager.AddScore(5);
            Debug.Log(ScoreManager.GetInstance().GetScore());
            // Debug.Log(scoreManager.GetScore());
        }
    }
}
```

```C#
// Singleton/ScoreAdder.cs

public class ScoreAdder : MonoBehaviour
{
    // public ScoreManager scoreManager;

    void Update() 
    {
        if(Input.GetMouseButtonDown(0))
        {
            ScoreManager.GetInstance().AddScore(5);
            // scoreManager.AddScore(5);
            Debug.Log(ScoreManager.GetInstance().GetScore());
            // Debug.Log(scoreManager.GetScore());
        }
    }
}
```

```C#
// Singleton/ScoreSubtractor.cs

public class ScoreSubtractor : MonoBehaviour
{
    // public ScoreManager scoreManager;

    void Update()
    {
        if(Input.GetMouseButtonDown(1))
        {
            ScoreManager.GetInstance().AddScore(-2);
            // scoreManager.AddScore(-2);
            Debug.Log(ScoreManager.GetInstance().GetScore());
            // Debug.Log(scoreManager.GetScore());
        }
    }
}
```



## 9. 코루틴

> 중간에 대기 시간을 삽입할 수 있다.
>
> 비동기 방식으로 실행이 가능하다.

```C#
// Coroutine/Fade.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; // Image를 사용하기 위해 호출

public class Fade : MonoBehaviour
{
    public Image fadeImage;

    void Start()
    {
        // StartCoroutine("FadeIn"); // 원할 때 멈출 수 있다.
        StartCoroutine(FadeIn()); // 성능은 좋지만 임의로 멈출 수 없다.
    }

    // Coroutine은 IEnumerator를 반환하는 함수이다.
    IEnumerator FadeIn()
    {
        Color startColor = fadeImage.color;

        for(int i = 0; i < 100; i++)
        {
            startColor.a -= 0.01f; // a는 투명도, r,g,b는 red, green, blue
            fadeImage.color = startColor;
            yield return new WaitForSeconds(0.01f); // yield 위치에서 멈추고 0.01초를 기다린 후 재개한다.
        }
    }

}
```

```C#
// Coroutine/HelloCoroutine.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HelloCoroutine : MonoBehaviour
{
    void Start()
    {
        // Coroutine을 통해 함수를 비동기로 실행
        StartCoroutine("HelloUnity");
        StartCoroutine(HiCSharp());
        Debug.Log("End");
    }
    void Update()
    {
        if(Input.GetMouseButtonDown(0))
        {
            StopCoroutine("HelloUnity"); // "HelloUnity"로 썼을 때만 가능 HelloUnity()는 불가능
        }
    }

    IEnumerator HelloUnity() 
    {
        while(true)
        {
            Debug.Log("Hello");
            yield return new WaitForSeconds(3f);
            Debug.Log("Unity");
        }
    }

    IEnumerator HiCSharp()
    {
        Debug.Log("Hi");
        yield return new WaitForSeconds(5f);
        // yield return null; // 기다리지 않고 실행 가능
        Debug.Log("CSharp");
    }

}
```

