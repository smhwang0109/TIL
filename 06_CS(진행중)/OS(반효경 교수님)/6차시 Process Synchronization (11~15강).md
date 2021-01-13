# 6차시 Process Synchronization (11~15강)

## 11강 Process Synchronization 0

>  Process Synchronization 개요

![6-1](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-1.PNG)

![6-2](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-2.PNG)

![6-3](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-3.PNG)



![6-4](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-4.PNG)

- 해결법
  - 하던 프로세스를 다 끝내고 인터럽트 과정으로 넘어가도록 한다.

![6-5](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-5.PNG)

![6-6](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-6.PNG)

![6-7](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-7.PNG)



![6-8](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-8.PNG)



![6-9](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-9.PNG)



![6-10](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-10.PNG)



![6-11](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-11.PNG)

## 12강 Process Synchronization 1

>  Process Synchronization 알고리즘

![6-12](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-12.PNG)

![6-13](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-13.PNG)

- 단점
  - 한번씩 교대로 들어가야 한다.
  - 한 프로세스가 안들어가면 다른 프로세스도 한번 나와서 계속 못들어간다.

![6-14](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-14.PNG)

- 단점
  - 둘 다 flag가 true이면 아무도 못들어가고 있는다.

![6-15](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-15.PNG)

- 단점
  - 세가지 조건을 모두 만족하지만 다른 프로세스가 수행될 동안 while문을 계속돌고 있어야 한다는 단점이 있다. (Busy Waiting)

![6-16](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-16.PNG)

- 하드웨어 단에서 아예 읽고 쓰는 것을 하나의 instruction으로 만들면(Test_and_set) 간단히 해결이 가능하다. 
- while 문에서
  - lock == 0이면
    - 읽는 값은 0 이기 때문에 while 문은 통과하고 lock은 1이 된다.
  - lock == 1이면
    - 읽는 값이 1이기 때문에 while 문을 계속 돌며 기다린다.

## 13강 Process Synchronization 2

>  Process Synchronization 개요

![6-17](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-17.PNG)

![6-18](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-18.PNG)

 ![6-19](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-19.PNG)

![6-20](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-20.PNG)

![6-21](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-21.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)

![6-50](C:/Users/user/house/TIL/06_CS(진행중)/OS(반효경 교수님)/Images/6-50.PNG)



출처 : https://core.ewha.ac.kr/publicview/C0101020140404144354492628?vmode=f