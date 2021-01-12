# 01_Docker 특징 및 설치

## Docker의 특징

- 기존 문제점
  - 기존 가상 머신을 이용한 가상화 기술은 하이퍼바이저를 거치기 때문에 성능 손실이 발생
  - 라이브러리, 커널 등을 전부 포함하여 이미지의 크기가 너무 커짐
- Docker
  - 리눅스 자체 기능인 chroot, namespace, cgroup을 이용해 프로세스 단위의 격리 환경을 만들기 때문에 성능 손실이 거의 없음
  - 구동에 필요한 라이브러리 및 실행 파일만 존재하기 때문에 이미지 크기가 줄어듦
  - 장점
    1. docker 이미지만 서버에 전달하기 때문에 의존성을 고려할 필요가 없어 애플리케이션 개발과 배포가 편리해짐
    2. 특정 애플리케이션 단위로 관리하여 독립성과 확정성이 높아짐



## Docker 엔진 설치

### 리눅스

#### 확인 사항

1. 최신 버전 커널인지 버전 확인

   ```bash
   $ uname -r
   ```

2. 지원 기간 내에 있는 배포판인지 확인

3. 64비트 리눅스인지 확인

4. sudo 명령 사용하거나 root 권한을 가진 계정으로 진행

#### Ubuntu에 설치

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

$ apt-get update

$ apt-get install docker-ce
```



#### CentOS 7, RHEL 7

```bash
$ yum install -y yum-utils

$ yum-config-manager --add-repo\
https://download.docker.com/linux/centos/docker-ce.repo

$ yum install -y docker-ce

$ systemctl start docker
```



#### OS 모를 때(별로 좋지 않은 방법)

```bash
$ wget -q0- get.docker.com | sh
```



#### 설치 확인

```bash
$ docker info
```



### 윈도우, 맥 OS

Docker는 기본적으로 linux를 권장

윈도우, 맥은 2가지 방법이 존재

1. Docker Toolbox(과거)
2. Docker for Windows(Hyper-V), Docker for Mac OS X(xhyve)
   - 윈도우, 맥 OS의 자체 가상화 기술을 이용