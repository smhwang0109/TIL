# Section3. C# 프로그래밍-기본

## 3. 플레이어 조작(1/2)

```c#
// 게임이 처음 시작되었을 때 한번 실행
void Start () {}

// 화면이 한번 깜빡일 때 한번 실행
// 영화 초당 24프레임
// 모바일, 콘솔 게임 30프레임/1s 
// PC 60프레임/1s
// 단, 사양에 따라 다르다.
void Update () {}

// 둘 다 메시지이다.
```

```C#
// Player.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Player : MonoBehaviour
{
    public float speed = 10f;
    public Rigidbody playerRigidbody;
    
    void Start()
    {

    }
    void Update()
    {
        // 유저 입력
        if(Input.GetKey(KeyCode.W))
        {
            playerRigidbody.AddForce(0,0,speed);
        }
        if(Input.GetKey(KeyCode.A))
        {
            playerRigidbody.AddForce(-speed, 0, 0);
        }
        if(Input.GetKey(KeyCode.S))
        {
            playerRigidbody.AddForce(0, 0, -speed);
        }
        if(Input.GetKey(KeyCode.D))
        {
            playerRigidbody.AddForce(speed, 0, 0);
        }
    }
}
```

- W,A,S,D로 조작 가능
- But, 너무 Hard Coding이다.



## 4. 플레이어 조작(2/2)

```C#
// Player.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Player : MonoBehaviour
{
    public float speed = 10f;
    public Rigidbody playerRigidbody;
    
    void Start()
    {
        // 게임 오브젝트에서 Rigidbody를 찾아서 할당한다.
        playerRigidbody = GetComponent<Rigidbody>();
        
        // generic : 특정 타입에 대해서 함수를 실행한다.
        // playerRigidbody = GetComponent<Rigidbody>();
        // Rigidbody에 대해서 GetComponent를 한다.
    }
    void Update()
    {
        
        // 발사 기능 - "Fire" - 마우스 왼쪽 버튼
        // 앉는 기능 - "Crunch" - 키보드 C
        // 점프 기능 - "Jump" - 키보드 스페이스
        
        // "Horizontal" -> 키보드 수평방향에 대응되는 키가 매핑되어 있음
        // A <-     0     -> D
        // -1.0     0     +1.0
        // 왜냐하면 조이스틱 때문에
        float inputX = Input.GetAxis("Horizontal");
        float inputZ = Input.GetAxis("Vertical");

        // 이렇게 사용하면 관성으로 인해 직관적인 조작이 어렵다.
        // playerRigidbody.AddForce(speed * inputX, 0, speed * inputZ);
        
        // 떨어지는 속도를 0으로 초기화하지 않고, 유지하기 위해
        float fallSpeed = playerRigidbody.velocity.y;

        // 힘(force)를 주지 않고 속도(velocity)를 바로 주면
        // 관성도 없고 직관적인 조작이 가능하다.
        Vector3 velocity = new Vector3(inputX, 0, inputZ);

        velocity = velocity * speed;
        velocity.y = fallSpeed;

        playerRigidbody.velocity = velocity;
    }
}

```



- Unity에서
  - Edit - Project Settings - Input Manager - Axes 에 가면 매핑 된 데이터들 확인 가능



##  7. 오브젝트 회전 + 시간 간격

```C#
// Rotator.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour
{
    // Update는 대략 1초에 60번
    void Update()
    {
        // public Transform transform; 과 같음
        // transform 은 나 자신의 transform을 가져온다.
        transform.Rotate(60 * Time.deltaTime, 60 * Time.deltaTime, 60 * Time.deltaTime);

        // Time.deltaTime 은 화면이 한번 깜빡이는 시간 = 한 프레임의 시간
        // 화면을 60번 깜박이면 (초당 60프레임) 1/60
        // 화면을 200번 깜박이면 (초당 200프레임) 1/200
        // 60/200 * 200 = 60/60 * 60 = 60
        // 즉, 컴퓨터 사양에 상관 없이 같은 정도로 회전할 수 있다.
    }
}

```



## 8. 충돌처리

```C#
// ItemBox.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemBox : MonoBehaviour
{

    private Renderer myRenderer;

    public Color touchColor;
    private Color originalColor;
    void Start()
    {
        myRenderer = GetComponent<Renderer>();
        originalColor = myRenderer.material.color;
    }

    void Update()
    {
        
    }

    // 트리거인 콜라이더와 충돌했을 때 자동으로 실행
    // collider의 isTrigger가 true로 되어 있는 오브젝트와 부딪쳤을 때
    // other에 충돌한 오브젝트를 할당한다.
    // 이 함수를 모든 오브젝트에 메시지로 보낸다.
    // OnTrigger 함수 중에서도
    // OnTriggerEnter는 충돌을 한 그 순간
    void OnTriggerEnter(Collider other)
    {
        if(other.tag == "EndPoint")
        {
            myRenderer.material.color = touchColor;
            Debug.Log("엔드포인트 도달!");
        }
    }

    // OnTriggerExit은 붙어있다가 떼어질 때
    void OnTriggerExit(Collider other)
    {
        if(other.tag == "EndPoint")
        {
            myRenderer.material.color = originalColor;
            Debug.Log("엔드포인트 도달!");
        }
    } 

    // OnTriggerStay는 충돌하고 있는 혹은 붙어 있는 동안
    void OnTriggerStay(Collider other)
    {
        if(other.tag == "EndPoint")
        {
            myRenderer.material.color = touchColor;
            Debug.Log("엔드포인트 도달!");
        }
    }

    // 일반 콜라이더와 충돌했을 때 자동으로 실행
    void OnCollisionEnter(Collision other)
    {
        
    }
}

```



## 9. 게임 매니저와 승리 조건

```C#
// GameManager.cs

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{

    // ItemBox Script를 배열로 받는다.
    public ItemBox[] ItemBoxes;

    public bool isGameOver;
    void Start()
    {
        isGameOver = false;
    }

    void Update()
    {

        if(isGameOver == true)
        {
            return;
        }

        int count = 0;
        for(int i = 0; i < 3; i++)
        {
            if(ItemBoxes[i].isOveraped)
            {
                count++;
            }
        }
        
        if(count >= 3)
        {
            Debug.Log("게임 승리!");
            isGameOver = true;
        }
    }
}

```



## 10. 승리 UI 추가

### UI 추가하기

- Hierarchy - 마우스 오른쪽 - UI - Text 추가
- Canvas : 만든 게임 오브젝트들과 상관없이 사용자에게 보이는 화면
- Text : 보여질 Text
- EventSystem : UI 요소들에게 유저의 입력을 전달하는 역할(건드리지 않아도 됨.)



```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{

    public GameObject winUI;
    public ItemBox[] ItemBoxes;

    public bool isGameOver;
    void Start()
    {
        isGameOver = false;
    }

    void Update()
    {

        if(Input.GetKeyDown(KeyCode.Space))
        {
            // using UnityEngine.SceneManagement;
            // 여기서 SceneManager 호출
            // SceneManager.LoadScene("Main");
            SceneManager.LoadScene(0);
        }

        if(isGameOver == true)
        {
            return;
        }

        int count = 0;
        for(int i = 0; i < 3; i++)
        {
            if(ItemBoxes[i].isOveraped)
            {
                count++;
            }
        }
        
        if(count >= 3)
        {
            Debug.Log("게임 승리!");
            isGameOver = true;
            winUI.SetActive(true);
        }
    }
}

```

