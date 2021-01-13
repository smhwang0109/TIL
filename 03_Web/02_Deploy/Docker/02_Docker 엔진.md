# 02_Docker 엔진

## 이미지와 컨테이너

### 이미지

컨테이너를 생성할 때 필요한 요소로 여러 개의 계층으로 된 바이너리 파일로 존재하고, 컨테이너를 생성하고 실행할 때 읽기 전용으로 사용된다. 보통 [저장소(repository) 이름]/[이미지 이름]:[태그(버전/리비전)] 형태로 구성한다.

```
ex) alicek106/ubuntu:14.04
```



### 컨테이너

다양한 종류의 이미지로 생성되며, 이미지의 목적에 맞는 파일이 들어 있는 파일 시스템과 격리된 시스템 자원 및 네트워크를 사용할 수 있는 독립된 공간.

컨테이너는 이미지를 읽기 전용으로만 사용하고, 이미지에서 변경된 사항만 컨테이너 계층에 저장하므로 컨테이너에서 무엇을 하든지 원래 이미지는 영향을 받지 않는다. 또한 독립된 공간이기 때문에 다른 컨테이너와 호스트에도 변화가 없다.



## 컨테이너 사용법

### 컨테이너 조회, 생성, 수정, 삭제

```bash
$ docker -v # docker 버전 확인

$ docker pull ubuntu:17.10 # 이미지 다운로드
$ docker create -i -t --name myubuntu ubuntu:17.10 # 컨테이너 생성 (-i -t : 컨테이너와 상호 입출력 가능하게 함 == bash 창을 사용 가능하게 함)
$ docker start myubuntu # 컨테이너 시작
$ docker attach myubuntu # 컨테이너로 들어가기

$ docker run -i -t --name myubuntu ubuntu:17.10 # pull + create + start + attach

# Ctrl + D / exit : 컨테이너 종료 후 나오기
# Ctrl + P, Q : 컨테이너 유지 후 나오기

$ docker ps # 현재 실행 중인 컨테이너 목록 확인
$ docker ps -a # 전체 컨테이너 목록 확인

$ docker rename myubuntu renameubuntu # 컨테이너 이름 변경

$ docker stop myubuntu # 컨테이너 중지
$ docker rm myubuntu # 컨테이너 삭제 (실행 중이지 않은 상태에서만 가능)
$ docker rm -f myubuntu # 컨테이너 강제 삭제
$ docker container prune # 컨테이너 전체 삭제 (사용 안하는걸 추천)

$ docker exec {컨테이너이름} {명령어} # 해당 컨테이너에 명령어 실행
$ docker exec myubuntu ls # myubuntu 컨테이너에 ls 명령어 실행
```



### 컨테이너 외부 노출

```bash
$ ifconfig # 컨테이너 네트워크 인터페이스 확인

# 호스트 3306 포트와 컨테이너 3306 포트, 호스트 192.168.0.100:7777 포트와 컨테이너 80 포트를 연결
$ docker run -i -t --name myubuntu -p 3306:3306 -p 192.168.0.100:7777:80 ubuntu:17.10 
```



