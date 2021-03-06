# Section2. 게임엔진의 원리

## 1. 게임 오브젝트와 컴포넌트

### 게임 오브젝트 

- 단순 홀더(Holder), 빈 껍데기



### 컴포넌트

- 미리 만들어진 부품
- 각자 대표 기능을 가진다.
- 스스로 동작하는 독립 부품

- 장점
  - 유연한 재사용
  - 기획자의 프로그래머 의존도가 낮아짐
  - 독립성 덕분에 추가와 삭제가 쉽다.



## 2. 메시지와 브로드캐스팅

### MonoBehaviour

- 유니티에서 미리만들어진 컴포넌트
- 컴포넌트로서 동작하기 위해 필요한 기능들을 제공
- 컴포넌트로서 게임 오브젝트에 추가될 수 있다.
- 유니티의 통제를 받는다.
- 유니티 이벤트 메시지를 감지할 수 있게 된다.



### 메시지

- 실행해야 될 기능을 담고 있는 정보
- 보내는 쪽은 누가 받는지 신경 안쓴다.
- 받는 쪽도 누가 보냈는지 신경 안쓴다.
- 메시지에 명시된 기능을 가지고 있으면 실행, 없으면 무시한다.



### 브로드 캐스팅

- 메시지를 모든 게임 오브젝트들에게 무차별적으로 많이 보내는 것



### 메시지/브로드 캐스팅 시스템

- 복잡한 참조 관계를 끊고, 라이프싸이클을 스스로 관리할 수 있게 한다.



### 유니티 이벤트 메서드(함수)

- 이름만 맞춰 구현하면, 해당 타이밍에 자동으로 실행된다.
- ex) Start, Awake, Update, OnTriggerEnter

