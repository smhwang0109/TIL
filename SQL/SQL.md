# SQL(Structured Query Language)

sqlite 생성

- sqlite3 데이터베이스이름.sqlite3



## DDL (데이터 정의 언어)

### CREATE

```SQL
CREATE TABLE 테이블명 (칼럼명 옵션);

-- 부서
CREATE TABLE DEPT (
	deptno varchar2(4) PRIMARY KEY,
    deptname varchar2(20)
);

-- 직원
CREATE TABLE EMP (
	empno number(10),
    ename varchar2(20),
    sal number(10,2) default 0,
    deptno varchar2(4) NOT NULL,
    createdate date default SYSDATE,
    CONSTRAINT e_pk PRIMARY KEY (empno),
    CONSTRAINT d_fk FOREIGN KEY (deptno)
    	REFERENCES dept(deptno)
    	ON DELETE CASCADE
);
```



### ALTER

```SQL
-- 테이블명 변경
ALTER TABLE 테이블명
RENAME TO 새 테이블 명;

-- 칼럼 추가
ALTER TABLE 테이블명
ADD (칼럼);

-- 칼럼 변경
ALTER TABLE 테이블명
MODIFY (칼럼);

-- 칼럼 삭제
ALTER TABLE 테이블명
DROP COLUMN 칼럼명;

-- 컬럼명 변경
ALTER TABLE 테이블명
RENAME COLUMN 기존칼럼명 TO 새칼럼명;
```



### DROP

```SQL
DROP TABLE 테이블명 CASCADE CONSTRAINT; -- 해당 테이블을 참조한 슬레이브 테이블과 관련된 제약사항도 삭제
```



### VIEW

> 가상의 테이블로 실제 데이터를 가지고 있지 않고 참조해서 원하는 칼럼만 조회
>
> 변경 불가능

```SQL
-- 뷰 생성
CREATE VIEW 뷰이름 AS
SELECT * FROM 테이블명;

-- 뷰 제거
DROP VIEW 뷰이름;
```



## DML (데이터 조작 언어)

```sql
SELECT * FROM 테이블명 WHERE 조건;

INSERT INTO 테이블명 VALUES 삽입할 레코드

UPDATE 테이블명 SET 수정할 데이터 WHERE 수정할 레코드;

DELETE FROM 테이블명 WHERE 삭제할 레코드;
```



### INSERT

```SQL
INSERT INTO 테이블명[(칼럼, 칼럼)] VALUES(칼럼내용, 칼럼내용);
```



### UPDATE

```SQL
UPDATE 테이블명 SET 칼럼명=바꾼후레코드 [WHERE 칼럼명=기존레코드;]; -- WHERE 입력 안하면 모든 데이터가 수정된다.
```



### DELETE

```SQL
DELETE FROM 테이블명 [WHERE 칼럼명=레코드]; -- WHERE 입력 안하면 테이블 내의 모든 레코드 삭제
```





### SELECT

> 실행순서 FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY

```SQL
-- 기본
SELECT 칼럼 FROM 테이블명 WHERE 칼럼명=레코드

-- ORDER BY
SELECT 칼럼 FROM 테이블명
[WHERE 조건]
[ORDER BY 칼럼 [ASC/DESC], 칼럼 [ASC/DESC]]; -- [오름차순/내림차순]
-- ORDER BY는 데이터를 너무 많이 사용한다.
-- 힌트를 사용해서 인덱스 기준 내림차순 가능
-- EX)
SELECT /*+ INDEX_DESC(deptno)*/ *
FROM DEPT deptno;

-- DISTINCT
SELECT [DISTINCT(중복없이)]칼럼 FROM 테이블명
[WHERE 조건];

-- ALIAS
SELECT 칼럼 AS "별명" FROM 테이블명 바꿀테이블명
[WHERE 바꾼테이블명.칼럼명=레코드];

-- WHERE
SELECT 칼럼 FROM 테이블명 WHERE 칼럼 LIKE '와일드카드';
SELECT 칼럼 FROM 테이블명 WHERE 칼럼 LIKE '%2_' -- %는 여러개가 가능, _는 정확히 저 갯수만큼만 가능;
SELECT 칼럼 FROM 테이블명 WHERE 칼럼 BETWEEN A AND B;
SELECT 칼럼 FROM 테이블명 WHERE 칼럼 IN 리스트;
SELECT 칼럼 FROM 테이블명 WHERE (칼럼1, 칼럼2) IN ((칼럼1요소1, 칼럼2요소1), (칼럼1요소2, 칼럼2요소2));
SELECT 칼럼 FROM 테이블명 WHERE 칼럼 IS NULL; -- NULL값 조회

-- GROUP BY
SELECT 그룹화할칼럼1, 집계함수(칼럼2) FROM 테이블명 
GROUP BY 칼럼1
HAVING 집계함수와 조건; -- WHERE도 사용 가능하나 WHERE는 개별 행의 조건을 따져서 조건에 맞지 않는 행은 아예 넣지를 않는다.
-- EX)
SELECT DEPTNO, SUM(SAL) FROM EMP
GROUP BY DEPTNO
HAVING SUM(SAL) > 10000;
-- 집계함수 종류
COUNT()
SUM()
AVG()
MAX()/MIN()
STDDEC() -- 표준편차
VARIAN() -- 분산

-- COUNT
SELECT COUNT(*) FROM 테이블명;    -- NULL 값을 포함한 행의 수
SELECT COUNT(칼럼) FROM 테이블명;  -- NULL 값을 제외한 행의 수

SELECT AVG(칼럼) FROM 테이블명;
SELECT SUM(칼럼) FROM 테이블명;
SELECT MAX(칼럼) FROM 테이블명;
SELECT MIN(칼럼) FROM 테이블명;

-- LIMIT
SELECT 칼럼 FROM 테이블명 LIMIT 숫자 OFFSET 숫자;
```





## 형변환

### 명시적 형변환

```SQL
TO_NUMBER(문자열)

TO_CHAR(숫자 혹은 날짜, [FORMAT]) -- FORMAT의 문자로 변환

TO_DATE(문자열, [FORMAT])
```



### 암시적 형변환

```SQL
-- EX)
SELECT *
FROM EMP
WHERE EMPNO='100';

-- EMPNO는 숫자형으로 지정해 놨기 때문에 TO_CHAR로 암시적 형변환을 해서 비교함
-- 하지만 암시적 형변환은 인덱스를 사용할 수는 없음

SELECT *
FROM EMP
WHERE EMPNO=TO_NUMBER('100')

-- 명시적 형변환으로 인덱스를 사용할 수 있음
```



## 내장형 함수

> 형변환 함수, 문자열 및 숫자형 함수, 날짜형 함수



### 문자열 함수

```SQL
ASCII(문자)

CHAR(ASCII 코드값)

SUBSTR(문자열, M, N) -- M번째부터 N개

CONCAT(문자열1, 문자열2) -- 문자열 합치기

UPPER/LOWER(문자열)

LENGTH 혹은 LEN(문자열)

RTRIM/LTRIM(문자열, 지정 문자)

TRIM(문자열, 지정 문자) -- 양쪽에서 지정 문자 삭제
```



### 날짜형 함수

```SQL
SYSDATE -- 오늘 날짜

EXTRACT(YEAR FROM SYSDATE)  -- 연도 가져오기

TO_CHAR(SYSDATE, 'YYYY/MM/DD')  -- 날짜 변환 포맷
```



### 숫자형 함수

```SQL
ABS()

SIGN()

MOD(숫자1, 숫자2)  --나눗셈

CEIL/CEILING()

FLOOR()

ROUND(숫자, M)  -- 소수점 M자리에서 반올림

TRUNC(숫자, M)  -- 소수점 M자리에서 절삭
```















***Tip**

정렬 깔끔하게 하는법

```sql
.headers on
.mode column
SELECT * FROM flights;
```

csv파일 불러오기

```sql
.mode csv
.import 파일명(ex)users.csv 테이블명(ex)users_user
```

