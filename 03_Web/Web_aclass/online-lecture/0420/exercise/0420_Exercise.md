# 0420_Exercise

1. flights 테이블을 생성하시오.

   ```sql
   CREATE TABLE flights (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       flight_num TEXT NOT NULL,
       departure TEXT NOT NULL,
       waypoint TEXT NOT NULL,
       arrival TEXT NOT NULL,
       price INTEGER NOT NULL
   );
   ```

   

2. 데이터를 입력하시오.

   ```sql
   INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   VALUES ('RT9122', 'Madrid', 'Beijing', 'Incheon', 200);
   
   INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   VALUES ('XZ0352', 'LA', 'Moscow', 'Incheon', 800);
   
   INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   VALUES ('SQ0972', 'London', 'Beijing', 'Sydney', 500);
   ```

   

3. flights 테이블 전체 데이터를 조회하시오.

   ```sql
   SELECT * FROM flights;
   ```

   

4. 모든 waypoint를 조회하시오.

   ```sql
   SELECT DISTINCT waypoint FROM flights;
   ```

   

5. 항공권 가격이 600 미만인 항공편들의 id와 flight_num을 조회하시오.

   ```sql
   SELECT id, flight_num FROM flights WHERE price < 600;
   ```

   

6. 도착지가 Incheon이고 가격이 500 이상인 항공편의 departure를 조회하시오.

   ```sql
   SELECT departure FROM flights WHERE arrival = 'Incheon' AND price >= 500;
   ```

   

7. 항공편의 숫자부분이 0으로 시작하고 2로 끝나면서 경유지가 Beijing인 항공편들의 id와 flight_num을 조회하시오.

   ```sql
   SELECT id, flight_num FROM flights WHERE flight_num LIKE '__0%2' AND waypoint = 'Beijing';
   ```

   

8. 항공편 SQ0972의 경유지를 Tokyo로 수정하시오.

   ```sql
   UPDATE flights SET waypoint = 'Tokyo' WHERE flight_num = 'SQ0972';
   ```

   

9. 항공편 RT9122를 테이블에서 삭제하시오.

   ```sql
   DELETE FROM flights WHERE flight_num = 'RT9122';
   ```

   

10. flights 테이블을 삭제하시오.

    ```sql
    DROP TABLE flights;
    ```

    