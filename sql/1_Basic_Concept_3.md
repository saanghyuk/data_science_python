# Basic Concept 3

- #### 데이터의 특성 구하기

  데이터의 특성을 분석해보자. 

  총 row수는 몇개일까? 

  ```sql
  SELECT COUNT(email) FROM copang_main.member;
  ```

  *여기서 중요한 것은 COUNT는 NULL의 갯수는 제외하고 셈.*

  

  테이블의 정확한 row수를 보고 싶을 때는?

  ```sql
  SELECT COUNT(height) FROM copang_main.member;
  ```

  회원들의 키 중에서 가장 큰 키는?

  ```sql
  SELECT MAX(height) FROM copang_main.member;
  ```

  몸무게 가장 적은 사람은?

  ```sql
  SELECT MIN(weight) FROM copang_main.member;
  ```

  회원들의 평균 몸무게는?

  그런데 평균을 구할 때 중요한 것이 있음. **NULL은?** 

  AVG는 NULL을 제외하고 계산함. 

  ```sql
  SELECT AVG(weight) FROM copang_main.member;
  ```

- #### 집계 함수와 산술 함수

  이전 영상에서는 한 컬럼의 

  개수(**COUNT**)

  최댓값(**MAX**)

  최솟값(**MIN**)

  평균값(**AVG**)

  을 구하는 함수들을 배웠습니다. 이 함수들처럼 **어떤 컬럼의 값들을 대상으로 원하는 특징값을 구해주는 함수**를 **Aggregate Function**, 우리말로는 **집계 함수**라고 합니다. 집계 함수에는 이전 영상에서 배운 것 말고도 

  모든 값의 합을 구하는 **SUM** 함수, 

  모든 값의 표준편차를 구하는 **STD** 함수 등이 있습니다. 각각 다음과 같습니다.

  **1. SUM 함수 - 합계**

  ![1_135](./resources/1_135.png)

  **2. STD 함수 - 표준편차**

  ![1_135](./resources/1_136.png)

  그런데 SQL에는 집계 함수 말고도, 단순한 산술 연산을 해주는 **Mathematical Function**들도 있습니다. 우리 말로 **'산술 함수'**라고 할 수 있는데요. 산술 함수에는 다음과 같은 것들이 있습니다.

  **ABS 함수 - 절대값을 구하는 함수**

  **SQRT 함수 - 제곱근을 구하는 함수** 

  **CEIL 함수 - 올림 함수**

  ![1_135](./resources/1_137.png)

  **3. FLOOR 함수 - 내림 함수**

  ![1_135](./resources/1_138.png)

  **4. ROUND 함수 - 반올림 함수**

  ![1_135](./resources/1_139.png)

  이것 말고도 또 다양한 산술 함수들이 있는데요. 그밖의 다양한 산술 함수들이 궁금하신 분들은 [이 링크](https://dev.mysql.com/doc/refman/8.0/en/mathematical-functions.html)를 참조하세요. 

  그렇다면 집계 함수와 산술 함수는 정확히 어떤 차이점이 있을까요? 둘의 차이점은

  ***(1) 집계 함수는 특정 컬럼의 여러 row의 값들을 동시에 고려해서 실행되는 함수이고***

  ***(2) 산술 함수는 특정 컬럼의 각 row의 값마다 실행되는 함수***

  라는 점입니다.

  예를 들어 집계 함수인 **MAX** 함수를 생각해보세요. 특정 컬럼의 값 중에서 최댓값을 구하려면 당연히 여러 row의 값들을 동시에 고려해야겠죠?

  하지만 **ABS**, **ROUND** 같은 산술 함수들은 그렇지 않습니다. 이 함수들은 그냥 특정 컬럼의 각 row의 값들에 대해 **각각** 실행될 뿐입니다.

  이 둘이 어떤 차이가 있는지 잘 아시겠죠? 데이터 분석을 할 때 숫자값을 자유롭게 다루려면 이 집계 함수와 산술 함수를 많이 알면 알수록 좋습니다. 특히 이번 토픽에서 배운 함수들을 잘 익혀둔다면 도움이 되겠죠? 



- #### NULL을 다루는 방법

  어떤 데이터를 분석해도, NULL은 자주 볼 수 있음. 

  ![1_135](./resources/1_140.png)

  adressd에 **NULL이 있는 Row들만 조회해 보자.**

  ```sql
  SELECT * FROM copang_main.member WHERE address IS NULL;
  ```

  adress에 **NULL이 없는 Row들만 조회하기** 

  ```sql
  SELECT * FROM copang_main.member WHERE address IS NOT NULL;
  ```

  height, address, weight 중에 하나라도 NULL이 있는 row들을 조회하려면? 

  ```sql
  SELECT * FROM copang_main.member 
  WHERE address IS NULL 
  	OR height IS NULL 
    OR weight IS NULL ;
  ```

  **NULL을 다른 값으로 바꿔주자.**

  **COALESCE** : 예를 들어 

  ```sql
  COALESCE(height, '####')
  ```

  라고 쓰면, height컬럼을 첫번째 부터 살펴본 다음에, 그 값이 있으면, 그대로 돌려주고 NULL이면, 뒤에 있는 값으로 바꿔주는 함수. 

  ```sql
  SELECT 
  	COALESCE(height, '####'),
      COALESCE(weight, '----'),
      COALESCE(height, '@@@')
  FROM copang_main.member ;
  ```

  

