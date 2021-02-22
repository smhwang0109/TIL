# 2. Docker 엔진

## 2-1. 이미지와 컨테이너

### 2-1-1. 이미지

컨테이너를 생성할 때 필요한 요소로 여러 개의 계층으로 된 바이너리 파일로 존재하고, 컨테이너를 생성하고 실행할 때 읽기 전용으로 사용된다. 보통 [저장소(repository) 이름]/[이미지 이름]:[태그(버전/리비전)] 형태로 구성한다.

```
ex) alicek106/ubuntu:14.04
```



### 2-1-2. 컨테이너

다양한 종류의 이미지로 생성되며, 이미지의 목적에 맞는 파일이 들어 있는 파일 시스템과 격리된 시스템 자원 및 네트워크를 사용할 수 있는 독립된 공간.

컨테이너는 이미지를 읽기 전용으로만 사용하고, 이미지에서 변경된 사항만 컨테이너 계층에 저장하므로 컨테이너에서 무엇을 하든지 원래 이미지는 영향을 받지 않는다. 또한 독립된 공간이기 때문에 다른 컨테이너와 호스트에도 변화가 없다.



## 2-2. 컨테이너 사용법

### 2-2-1. 컨테이너 조회, 생성, 수정, 삭제

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



### 2-2-2. 컨테이너 외부 노출

```bash
$ ifconfig # 컨테이너 네트워크 인터페이스 확인

# 호스트 3306 포트와 컨테이너 3306 포트, 호스트 192.168.0.100:7777 포트와 컨테이너 80 포트를 연결
$ docker run -i -t --name myubuntu -p 3306:3306 -p 192.168.0.100:7777:80 ubuntu:17.10 
```



### 2-2-3. Docker 볼륨

#### 2-2-3-1. 호스트 볼륨 공유

> 호스트에 있는 디렉터리를 컨테이너의 폴더에서 공유 (-v 옵션)

```bash
$ docker run -d --name wordpressdb_hostvolume -e MYSQL_ROOT_PASSWORD=password\
  -v /home/wordpress_db:/var/lib/mysql mysql:5.7 # -v [호스트의 공유 디렉터리]:[컨테이너의 공유 디렉터리]
```



#### 2-2-3-2. 볼륨 컨테이너

> 볼륨을 사용하는 컨테이너를 다른 컨테이너와 공유(--volume-from)

```bash
$ docker run -i -t --name volumes_from_container\
  --volume-from volume_overide ubuntu:17.10
```



#### 2-2-3-3. 도커 볼륨

> 도커 자체에서 제공하는 볼륨 기능(docker volume)
>
> 도커 엔진에서 관리

```bash
$ docker volume create --name myvolume

$ docker volume ls

$ docker run -i -t --name myvolume_1 \
-v myvolume:/root/ ubuntu:17.10 # -v [볼륨의 이름][컨테이너의 공유 디렉터리] (호스트 볼륨 공유와 같이 -v를 쓰지만 방식이 다르다.)

$ docker inspect --type volume myvolume # 볼륨 내용 표시

$ docker volume prune # 도커 볼륨 모두 삭제
```



### 2-2-4. Docker 네트워크

도커는 각 컨테이너에 외부와의 네트워크를 제공하기 위해 컨테이너마다 가상 네트워크 인터페이스를 호스트에 생성하며  이 인터페이스의 이름은 veth로 시작한다. veth 인터페이스는 사용자가 직접 생성할 필요 없고, 컨테이너가 생성될 때 도커 엔진이 자동으로 생성한다.

```bash
$ ifconfig # 윈도우는 ipconfig

or

$ ip addr

# 네트워크 인터페이스를 확인하면 실행 중인 컨테이너 수만큼 veth로 시작하는 인터페이스가 생성
# eth0 : 실제로 외부와 통신할 수 있는 호스트의 네트워크 인터페이스
# veth... : 각 컨테이너의 eth0와 연결되어 있음
# docker0 : 각 veth 인터페이스와 바인딩 되어 eth0 인터페이스와 이어주는 브릿지

$ brctl show docker0 # docker0과 veth가 실제로 연결되었는지 확인 가능
```



#### 2-2-4-1. 도커 네트워크 기능

```bash
$ docker network ls # 도커에서 사용가능한 네트워크 종류 조회

$ docker network inspect bridge
```



##### 브릿지 네트워크

> docker0이 아닌 사용자 정의 브리지를 새로 생성해 각 컨테이너에 연결하는 네트워크 구조
>
> 기본적으로는 컨테이너를 생성할 때 자동으로 연결되는 docker0 브릿지를 활용하도록 설정되어 있다.

```bash
$ docker network create --driver bridge mybridge # 브릿지 생성

$ docker run -i -t --name mynetwork_container\
  --net mybridge ubuntu:17.10
  
$ docker network disconnect mybirdge mynetwork_container # 네트워크 연결 해제
$ docker network connect mybirdge mynetwork_container # 네트워크 연결
# connect와 disconnect는 특정 IP 대역을 갖는 네트워크 모드에만 적용이 가능

# network 생성 시 다양한 요소를 직접 설정이 가능하다.
$ docker network create --driver=bridge \
  --subnet=172.72.0.0/16 \
  --ip-range=172.72.0.0/24 \ # --subnet과 --ip-rang는 같은 대역이어야 한다.
  --gateway=172.72.0.1/1 \
  my_custom_network
```



##### 호스트 네트워크

> 새로 생성할 필요 없이 기존의 host라는 이름의 네트워크를 사용하여 호스트의 네트워크 환경을 그대로 사용할 수 있다.

```bash
$ docker run -i -t --name network_host\
  --net host ubuntu:17.10
```



##### 논 네트워크

> 말 그대로 아무 네트워크도 사용하지 않는 것을 의미. (외부와의 연결이 단절)

```bash
$ docker run -i -t --name network_none \
  --net none ubuntu:17.10
```



##### 컨테이너 네트워크

> 다른 컨테이너의 네트워크 네임스페이스 환경을 공유 (내부 IP, 맥(MAC) 주소 등)

```bash
$ docker run -i -t --name network_container \
  --net container:network_host ubuntu:17.10
```



##### 브릿지 네트워크와 --net-alias

> 각 컨테이너의 네트워크에 alias(별명)를 붙여서 여러 컨테이너의 네트워크에 접근할 수 있다.

```bash
# 같은 alias로 3개의 컨테이너를 만듦
$ docker run -i -t -d --name network_alias_container1 \
  --net mybridge --net-alias soom101 ubuntu:17.10
  
$ docker run -i -t -d --name network_alias_container2 \
  --net mybridge --net-alias soom101 ubuntu:17.10

$ docker run -i -t -d --name network_alias_container3 \
  --net mybridge --net-alias soom101 ubuntu:17.10

# ping 보낼 컨테이너 생성
$ docker run -i -t --name network_alias_ping \ 
  --net mybridge ubuntu:17.10
  
root@16ad51cd5e:/# ping -c 1 soom101 
# 요청을 보낼 때 마다 다른 3가지 컨테이너가 라운드로빈(하나의 CPU를 여러 프로세스들이 우선순위 없이 돌아가며 할당받는 방식) 방식으로 결정되어 하나씩 나옴.
# 이는 도커의 DNS가 호스트 이름으로 유동적인 컨테이너의 IP를 찾아주기 때문.

# dig 명령어로 DNS에 있는 도메인 이름에 대응하는 IP를 조회할 수 있음.
root@16dg51sdg5s:/# apt-get update
root@16dg51sdg5s:/# apt-get install dnsutils
root@16dg51sdg5s:/# dig soom101 # 반복해서 조회 시 매번 IP 리스트 순서가 바뀜. (라운드로빈)
```



##### MacVLAN 네트워크

호스트의 네트워크 인터페이스 카드를 가상화해 물리 네트워크 환경을 컨테이너에게 동일하게 제공한다. 이를 통해 컨테이너는 물리 네트워크상에서 가상의 맥(MAC) 주소를 가지며, 해당 네트워크에 연결된 다른 장치와의 통신이 가능해진다. MacVLAN에 연결된 컨테이너는 기본적으로 할당되는 IP 대역 172.17.X.X 대신 네트워크 장비의 IP를 할당받기 때문이다.

단, MacVLAN 네트워크를 사용하는 컨테이너는 기본적으로 본인의 호스트와 통신이 불가능하다.



### 2-2-5. 컨테이너 로깅

#### 2-2-5-1. json-file 로그 사용하기

> 도커는 컨테이너의 표준 출력(StdOut)과 에러(StdErr) 로그를 별도의 메타데이터 파일로 저장하며 이를 확인하는 명령어를 제공한다.

```bash
$ docker logs {컨테이너이름}
# options
# --tail 10 : 마지막 줄부터 10번째 줄까지 출력
# --since 1474765979 : 유닉스 시간(1474765979) 이후의 로그 출력
# -t : 타임스탬프 출력
# -f : 실시간 로그 출력

```

기본적으로 컨테이너 로그는 JSON 형태로 도커 내부에 저장된다.

```bash
# 저장 경로
$ /var/lib/docker/containers/${CONTAINER_ID}/${CONTAINER_ID}-json.log
```

파일이 너무 커지는 것을 방지하기 위해 조치한다.

```bash
$ docker run -it \
--log-opt max-size=10k\ # 파일의 최대 크기
--log-opt max-file=3\ # 파일의 개수
--log-driver=syslog\ # json 외에 다양한 로깅 드라이버 (syslog, journald, fluetd, awslogs 등)
--name log-test ubuntu:17.10
```



***** 참고

도커 데몬 시작 옵션에서 기본적으로 사용할 로깅 옵션 설정 변경 가능

```bash
DOCKER_OPTS="--log-driver=syslog"
DOCKER_OPTS="--log-opt max-size=10k --log-opt max-file=3"
```



#### 2-2-5-2. syslog 로그

