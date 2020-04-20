# SQL(Structured Query Language)

sqlite 생성

- sqlite3 데이터베이스이름.sqlite3

```SQL
DDL 데이터 정의 언어

CREATE TABLE 테이블명 (칼럼명 옵션);

DROP TABLE 테이블명;

DML 데이터 조작 언어

SELECT * FROM 테이블명 WHERE 조건;

INSERT INTO 테이블명 VALUES 삽입할 레코드

UPDATE 테이블명 SET 수정할 데이터 WHERE 수정할 레코드;

DELETE FROM 테이블명 WHERE 삭제할 레코드;
```



### SELECT

```SQL
SELECT [DISTINCT(중복없이)]컬럼 FROM 테이블명
[WHERE 조건]
[GROUP BY 컬럼]
[ORDER BY 컬럼 [ASC/DESC]]
[LIMIT 숫자]

SELECT COUNT(컬럼) FROM 테이블명
SELECT AVG(컬럼) FROM 테이블명
SELECT SUM(컬럼) FROM 테이블명
SELECT MAX(컬럼) FROM 테이블명
SELECT MIN(컬럼) FROM 테이블명

SELECT 컬럼 FROM 테이블명 WHERE 컬럼 LIKE '와일드카드'
SELECT 컬럼 FROM 테이블명 LIMIT 숫자 OFFSET 숫자
```





***Tip**

정렬 깔끔하게 하는법

```sql
.headers on
.mode column
SELECT * FROM flights;
```





# DB

1. 관계없음

2. 1:1

3. 1:N

4. M:N

   