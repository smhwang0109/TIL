



# 5차시 CPU Scheduling (9~11강)

## 9강 CPU Scheduling 0

>  CPU Scheduling 개요

![5-1](./Images/5-1.PNG)

- CPU burst : CPU만 사용하는 과정
- I/O burst : I/O만 사용하는 과정



![5-2](./Images/5-2.PNG)



- CPU bound job : CPU를 가장 많이 쓰는 업무
- I/O bound job : I/O를 많이 쓰고 CPU를 짧게 쓰는 업무







![5-3](./Images/5-3.PNG)



![5-4](./Images/5-4.PNG)

- CPU Scheduler
  - 운영체제 커널에 있는 코드
  - CPU를 누구한테 줄지 결정
- Dispatcher
  - 운영체제 커널에 있는 코드
  - CPU를 넘겨주는 과정을 담당





## 10강 CPU Scheduling 1

> CPU Scheduling 종류



### CPU Scheduling의 성능 척도

![5-5](./Images/5-5.PNG)



![4-6](./Images/4-6.PNG)





![4-7](./Images/4-7.PNG)



- exec은 fork 없이도 가능하다.

- main함수의 execlp 이후의 코드는 실행이 불가능하다.



#### wait()

![4-8](./Images/4-8.PNG)

wait : 자식 프로세스가 종료될 때까지 기다리는 모델



#### exit()

![4-9](./Images/4-9.PNG)



### Process 간 협력

![4-10](./Images/4-10.PNG)



![4-11](./Images/4-11.PNG)



![4-12](./Images/4-12.PNG)

shared 메모리도 처음에는 kernel을 거쳐야 사용 가능











출처 : https://core.ewha.ac.kr/publicview/C0101020140325134428879622?vmode=f