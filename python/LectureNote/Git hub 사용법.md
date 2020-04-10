# Git hub  사용법

- git branch 
  - branch 조회
- git branch soom
  - brach 생성
- git switch [이동하고자 하는 브랜치명]
  - git switch soom
- git switch -c [이동하고자 하는 브랜치명]
  - branch 만들면서 이동
- git branch -d [브랜치명]
  - branch 지우기
- touch a.txt 
  - 파일 생성

- git merge [병합할 브랜치의 이름]
  - 병합할 브랜치(master)로 이동 후 merge 해야 한다.
  - git merge soom
    - FastForward - Merge
      - master 브랜치에 아무것도 추가하지 않고 다른 브랜치를 merge 할 때
    - Auto - Merge 
      - 개별  branch의 작업들이 충돌하지 않을 때
      - Merge 됐다는 commit이 하나 새로 나온다.
      - :wq 로 빔창 나온다.
    - Conflict Merge
      - 충돌난 commit  합친다.

- branch는 일회용이다.

  - 만든 branch는 merge 하고 삭제한다.

- git checkout [이동할 브랜치 이름]

  - == git switch [이동할 브랜치 이름]

- git checkout -b [이동할 브랜치 이름]

  - == git switch -c [이동할 브랜치 이름]

- git log --oneline --graph

  - 그래프로 보기

  