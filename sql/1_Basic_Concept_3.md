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

- #### NULL을 다른 값으로 변환하는 다양한 함수. 

  이전 영상 중에서 테이블에 존재하는 NULL을 다른 직군의 사람들도 잘 이해할 수 있도록 다른 표현으로 변환하는 방법을 배웠던 거, 기억나시죠? 그때는 **COALESCE 함수**를 사용했었는데요. MySQL에서 NULL을 다른 값으로 변환할 수 있는 방법에는 COALESCE 함수 말고 다른 것들도 있습니다.

  NULL을 다른 값으로 변환하는 방법들, 한번 정리해볼게요.

  **1. COALESCE 함수** 

  우리가 배웠던 COALESCE 함수입니다. 

  ![1_135](./resources/1_156.png)

  이전에 배웠던 것처럼 COALESCE 함수는 괄호 속 인자 중에서 가장 첫 번째로 NULL이 아닌 값을 반환합니다. 지금 저는 height 컬럼의 NULL들을 ‘N/A’라는 문자열로 교체했는데요. N/A는 Not Available, Not Applicable의 줄임말로 테이블에서 어떤 값이 없거나 표현할 수 없는 값일 때를 사용되는 단어입니다. 엑셀에서도 자주 등장하는 단어라 아무래도 NULL보다는 사람들이 좀더 많이 아는 단어일 겁니다. 

  그런데 COALESCE를 이렇게도 써볼 수 있습니다. 

  ![1_135](./resources/1_157.png)

  이번엔 COALESCE 함수 안에 **weight \* 2.3**이라는 식이 추가되었습니다. 지금 저는 사람의 키가 보통 몸무게에 2.3 을 곱한 값이라고 가정한 건데요. 만약 height 컬럼이 NULL이면, 해당 row의 weight 컬럼의 값을 갖고 키를 추론해본 겁니다. height 컬럼도 NULL이고, **weight 컬럼도 NULL인 row라면 ‘N/A’**가 출력됐을 겁니다. 결과를 보니까 다행히도 지금 height 컬럼과 weight 컬럼이 모두 NULL인 row는 없는 것 같네요. 

  만약 데이터 분석을 할 때 단 하나의 NULL도 허용할 수 없는 상황이라면, 이렇게 나름의 가정을 하고 NULL을 적절한 값으로 변환하는 것도 좋은 방법 중 하나입니다. 

  **2. IFNULL 함수**

  IFNULL 함수는 첫 번째 인자가 NULL인 경우에는, 두 번째 인자를 표시하고 NULL이 아니면 해당 값을 그대로 표현합니다. 아래 그림을 보시면 바로 이해되실 겁니다. 

  ![1_135](./resources/1_158.png)

  그러니까 height 컬럼이 NULL이면 'N/A'를 출력하고, NULL이 아니면 height 컬럼의 값을 그대로 출력하죠.

  **3. IF 함수**

  IF 함수는 가장 첫 번째 인자로 어떤 조건식이 옵니다. 만약 그 조건식의 결과가 True라면 두 번째 인자를 리턴하고, False라면 세 번째 인자를 리턴합니다. 아래 그림을 보면 바로 이해되실 텐데요.

  ![1_135](./resources/1_159.png)

  지금 height IS NOT NULL이 True인 경우, 그러니까 height 컬럼에 값이 있는 경우에는 그 값이 그대로 출력되고, False인 경우 그러니까 height 컬럼이 NULL인 경우는 'N/A'이 출력되는 겁니다.

  **4. CASE 함수** 

  CASE 함수는 이전에 배웠는데요. 아래 SQL 문처럼 CASE 함수로도 NULL을 적절한 값으로 변환해서 나타낼 수 있습니다. 아래 그림은 따로 설명하지 않아도 되겠죠?

  ![1_135](./resources/1_160.png)

- #### NULL에 관해 알아야 하는 사실들

  이전 영상에서는 NULL을 어떻게 다뤄야하는지 배웠습니다. 

  그런데 NULL에 관해서 꼭 알아두어야할 사실 두 가지가 있는데요.

  하나씩 설명할게요. 

  **1. IS NULL 과 = NULL은 다릅니다.**

  간혹 IS NULL을 써야할 자리에 = NULL이라고 쓰는 실수를 하는 분들이 있습니다. 그러니까 이렇게 써야할 SQL 문을 

  ![1_135](./resources/1_141.png)

  이렇게 써버리는 거죠.

  ![1_135](./resources/1_142.png)

  이런 실수를 하면, 위 그림에서 보이는 것처럼 아무 row도 출력되지 않습니다. 

  **NULL은 어떤 값이 아니기 때문에 애초에 등호(=)를 사용해서 어떤 값과 비교할 수 있는 대상이 아닙니다.** 그래서 = NULL은 절대 True일 수가 없죠. 그래서 IS NULL이라는 키워드가 별도로 마련된 겁니다. 앞으로 NULL인지를 확인할 때는 = NULL을 쓰면 안 되고, 반드시 **IS NULL**을 써야한다는 점을 꼭 기억하셔야 합니다.

  그럼 당연히 != NULL, <> NULL 같은 것도 쓸 수 없겠죠? 이 표현은 이전 영상에서 배운대로 **IS NOT NULL**이라고 나타내야 하는 겁니다. 

  이 부분은 NULL을 처음 배우는 분들히 흔히들 하는 실수니까 주의하세요.

  **2. NULL에는 어떤 연산을 해도 결국 NULL이다.**

  잠깐 member 테이블 전체를 조회해볼게요. 

  ![1_135](./resources/1_143.png)

  cowboy@codeit.kr이라는 회원의 height 컬럼에 NULL이 들어있죠? 만약 height 컬럼에 +3을 해서 조회한다면 이 NULL은 어떻게 보일까요?

  ![1_135](./resources/1_144.png)

  가장 오른쪽을 보면, 각 row의 height 컬럼의 값에 3을 더한 값이 담긴 새 컬럼이 추가돼서 보이네요. 그런데 지금 가장 오른쪽의 빨간색 박스를 보면 원래 height 컬럼이 NULL이었던 곳은 여전히 NULL인 것을 알 수 있는데요.

  사실 NULL에는 뭘 더하든, 빼든, 곱하든, 나누든지 간에 항상 NULL입니다. NULL이라는 것 자체가 값이 없음을 나타내는데 그것에 어떤 처리를 해봤자 결국 또 NULL일 수밖에 없는 거죠. 오히려 어떤 값이 도출되는 게 더 이상하겠죠? 이 사실은 곧 다른 영상에서도 다시 등장하니까 잘 기억하세요. 



- #### 이상한 값을 제외하고 싶다면?

  전체 회원의 평균 나이

  ```sql
  SELECT AVG(age) FROM copang_main.member;
  ```

  근데 생각해보면, 코팡은 2~30대를 타겟으로하는데, 평균나이가 43세가 나옴. 이상한가 잘 봐야돼. 

  음수값이나, 200, 300이런 값들이 있어서 그런 것. 

  ![1_135](./resources/1_145.png)

  ```sql
  SELECT * FROM copang_main.member WHERE age BETWEEN 5 AND 100;
  SELECT AVG(age) FROM copang_main.member WHERE age BETWEEN 5 AND 100;
  ```

  그럼 이제 address를 봐보자. 

  이상한 값들이 있음. 

  ![1_135](./resources/1_146.png)

  ```sql
  SELECT * FROM copang_main.member WHERE address NOT LIKE '%호';
  ```

  ![1_135](./resources/1_147.png)



- #### 실전 데이터 분석은 만만치 않아요!

  이전 영상들에서 우리는

  **(1) 컬럼의 값이 NULL이거나**

  **(2) 아예 이상한 값인 경우들을**

  살펴봤습니다.

  지금 여러분은 SQL을 배우는 단계이기 때문에, 코드잇에서 준비한 '학습용 데이터'를 사용하고 있는데요.

  실제로는 이렇게 NULL이 있거나, 이상한 값이 있는 경우가 그렇게 많지는 않습니다. 

  잠깐 어떤 서비스의 회원가입을 예로 들자면,

  실제 서비스에서는

  - 사용자로부터 반드시 획득해야하는 정보에 대해서는, 사용자가 꼭 입력을 해야만 
  - 그리고 입력된 값이 유효해야만(예를 들어, 나이 값이라면 0 이상 100이하여야 한다는 조건 등)

  회원가입이 승인되도록, 개발자들이 이미 프로그램 코드 상에서 방어를 해주기 때문입니다.

  하지만 생긴 지 오래된 서비스이거나, 시간이 촉박한 상황에서 급하게 만들어져 꼼꼼하게 개발되지 않은 서비스인 경우에는 고객으로부터 수집된 데이터가 완벽하지 않을 수도 있습니다.

  따라서 여러분 또한 불완전한 데이터(NULL, 이상한 값)를 가지고도 유의미한 인사이트(insight)를 도출할 수 있어야 합니다. 그리고 이전 영상들에서 배운 'NULL과 이상한 값을 적절하게 처리하는 방법'은 꼭 알아야하는 내용이구요. 

  여러분이 회사에서 

  - 불완전한 데이터 속에서도 유의미한 인사이트를 끌어내고 동시에 
  - 더 완벽한 데이터 수집을 위한 피드백을 개발팀에 전달할 수 있게 된다면 

  누구에게나 인정받는 사람이 될 수 있겠죠?



- #### 컬럼끼리 계산하기

  각 회원들의 BMI지수를 구해보자(*height를 100으로 나눈 것은, BMI를 구할 때 키는 M 단위여야 하기 때문* ). 

  ![1_135](./resources/1_148.png)

  ```sql
  SELECT email, height, weight ,  weight / ( (height/100) * (height/100) ) FROM copang_main.member
  ```

  **중요한 것은 위처럼 컬럼끼리 산술계산이 가능하다는 것.** 

  아래와 같은 연산들이 모두 가능함. 

  ![1_135](./resources/1_149.png)

  여기서 알아야 할 또 하나의 것은, 연산을 하는 두 컬럼중에 하나라도 NULL이 있는 row는 계산되지 않는다는 것. 결과도 무조건 NULL이 됨. 

  ![1_135](./resources/1_150.png)



- #### 컬럼에 alias 붙이기

  위에서 보면, BMI를 구했는데, 그 BMI를 계산한 컬럼의 이름이 계산 식이 그대로 나와서 보기 좋지 않음. 

  ![1_135](./resources/1_151.png)

  ```sql
  SELECT email, height, weight ,  weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member
  ```

  ```sql
  SELECT email, height AS 키, weight AS 몸무게,  weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member
  
  ```

  그런데 사실 **AS** 없이 스페이스 한칸만 붙여도, 가능함. 

  ```sql
  SELECT email, height 키, weight 몸무게,  weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member
  ```

  다만 되도록이면 AS를 쓰는 것이 가독성이 좋음. 

  **CONCAT은 합치는 함수**

  ```sql
  SELECT email, height AS 키, weight AS 몸무게,  weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member
  ```

  CONCAT은 연결하다 라는 뜻. 괄호안에 있는 것들을 이어서, 하나로 만들어줌. 

  ```sql
  SELECT email, CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
  weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member
  ```

  



- #### 칼럼 변환해서 보기

  ![1_135](./resources/1_152.png)

  ```sql
  SELECT email, CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
  weight / ( (height/100) * (height/100) ) AS BMI,
  
  CASE 
  	WHEN weight IS NULL OR height IS NULL THEN '비만여부 알 수 없음'
      WHEN weight / ((height/100)*(height/100)) >= 25 THEN '과체중 또는 비만'
      WHEN weight / ((height/100)*(height/100)) >= 18.5
  		AND weight/((height/100)*(height/100)) < 25
          THEN 정상
  	ELSE '저체중'
  END
  
  FROM copang_main.member
  ```

  ![1_135](./resources/1_153.png)

  OBESITY CHECK 로 컬럼 명 바꿔보자. 

  이렇게 긴 경우에는 case문 전체에 괄호를 씌워주고 하는 것이 좋음. 

  ```sql
  SELECT email, CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
  weight / ( (height/100) * (height/100) ) AS BMI,
  
  (CASE 
  	WHEN weight IS NULL OR height IS NULL THEN '비만여부 알 수 없음'
      WHEN weight / ((height/100)*(height/100)) >= 25 THEN '과체중 또는 비만'
      WHEN weight / ((height/100)*(height/100)) >= 18.5
  		AND weight/((height/100)*(height/100)) < 25
          THEN '정상'
  	ELSE '저체중'
  END) AS 'obesity_check'
  
  FROM copang_main.member
  
  ```

  여기서 이 컬럼을 기준으로 정렬까지 하면?

  ```sql
  SELECT email, CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
  weight / ( (height/100) * (height/100) ) AS BMI,
  
  (CASE 
  	WHEN weight IS NULL OR height IS NULL THEN '비만여부 알 수 없음'
      WHEN weight / ((height/100)*(height/100)) >= 25 THEN '과체중 또는 비만'
      WHEN weight / ((height/100)*(height/100)) >= 18.5
  		AND weight/((height/100)*(height/100)) < 25
          THEN '정상'
  	ELSE '저체중'
  END) AS 'obesity_check'
  
  FROM copang_main.member 
  ORDER BY obesity_check ASC;
  
  ```

  

- ####  CASE 함수의 종류

  이전 영상에서는 특정 값을 원하는 방식으로 변환해서 표현하게 해주는 CASE 함수를 배웠는데요.

  그런데 사실 CASE 함수에는 크게 2종류가 있습니다. **단순 CASE 함수**와 **검색 CASE 함수**가 있는데요. 하나씩 살펴볼게요.

  **1. 단순 CASE 함수**

  ```sql
  CASE 컬럼 이름 
    WHEN 값 THEN 값 
    WHEN 값 THEN 값
    WHEN 값 THEN 값
    ELSE 값
  END
  ```

  이런 식으로 작성된 CASE 함수를 단순 CASE 함수라고 하는데요. 바로 예시를 보여드릴게요. 

  ![1_135](./resources/1_154.png)

  지금 age 컬럼의 값이 

  29면 ‘스물 아홉 살’, 30이면 ‘서른 살’ 이라고 표현되도록 했습니다. 결과를 보니 잘 작동하죠?

  그리고 CASE 함수 중에서 ELSE age는 나머지 경우에는 모두 age 컬럼에 있던 값을 그대로 보여달라는 뜻입니다. 

  이렇게 CASE 문 바로 뒤에 컬럼 이름을 쓰고, 그 컬럼의 값과 어떤 값이 같은지(=)를 비교하는 CASE 함수를 **단순 CASE 함수**라고 합니다.

  **2. 검색 CASE 함수**

  ![1_135](./resources/1_155.png)

  위 그림처럼 우리가 이전 영상에서 배운 것이 바로 검색 CASE 함수입니다. 지금 CASE 함수의 형식을 보면 다음과 같죠?

  ```sql
  CASE 
    WHEN 조건1 THEN 값
    WHEN 조건2 THEN 값 
    WHEN 조건3 THEN 값 
    ELSE 값
  END 
  ```

  이전에 설명한 대로 이런 CASE 함수에서는 일단 TRUE인 조건을 만나게되면 거기에 있는 THEN 뒤의 값을 돌려주고, CASE 함수는 종료됩니다. 

  그럼 검색 CASE 함수는 단순 CASE 함수와 어떤 점이 다를까요? 일반적으로 단순 CASE 함수에서는 등호 연산(=) 밖에 할 수 없다는 단점이 있습니다. 하지만 검색 CASE 함수에서는 사용자가 직접 원하는 대로 조건을 설정할 수 있기 때문에 좀더 다양한 형태의 조건을 걸 수 있다는 장점이 있구요. 위 사진을 보면 BMI 값의 범위를 확인하는 조건들을 사용한 것을 볼 수 있는데요. 이건 등호 연산만 할 수 있는 단순 CASE 함수에서는 불가능한 일입니다.

  대부분 검색 CASE 함수를 사용하는 경우가 많지만, 여러분이 실무에서 보게될 기존 SQL 문에 단순 CASE 함수가 쓰여있을 수도 있기 때문에 알려드렸습니다.  

  

- #### alias를 붙이고 바로 쓸 수 없는 이유

  이전 영상에서는 컬럼 이름에 **alias**를 붙이는 방법을 배웠습니다. 이번 노트에서는 alias에 관해 알아두면 좋을 2가지 내용을 설명하겠습니다. 하나씩 설명할게요.

  **1. 띄어쓰기(스페이스)가 포함된 alias에는 따옴표를 붙여줘야 합니다.**

  만약 컬럼에 스페이스가 포함된 alias를 붙이고 싶다면, 작은 따옴표나 큰 따옴표를 붙여서 alias 부분을 확실하게 표현해주어야 합니다. 아래 그림을 보면 저는 name 컬럼에 '상품 이름'이라는 alias를 붙일 때, 작은따옴표를 붙였습니다. 

  ![1_135](./resources/1_161.png)

  이렇게 하지 않으면 스페이스를 기준으로 구문 해석이 이루어지는 SQL 특성상 에러가 발생하니까 주의하세요.   

  **2. SELECT 절에서 설정한 alias를 바로 사용할 수 없는 문제**

  이전 영상에서 봤던 장면을 잠깐 다시 보겠습니다.

  ![1_135](./resources/1_162.png)

  이전 영상에서 저는 height 컬럼과 weight 컬럼을 갖고 BMI 값을 계산했습니다. 

  그런데 이 SQL 문을 계속 보고 있다보면 한 가지 의문이 듭니다.

  지금 저는 SELECT 절 뒤에서 **weight / ((height/100) \* (height/100)) 에, BMI 라는 alias를 붙였죠?**

  그럼 그냥 CASE 함수 안에서도 저렇게 긴 BMI 공식을 표시할 필요없이 바로 BMI라고 쓰면 안 될까요?

  길다란 공식 부분을 모두 BMI라고 수정하고 다시 실행해보겠습니다.

  ![1_135](./resources/1_163.png)

  그런데 실행이 되지 않습니다.

  실행 결과창을 보면 

  ![1_135](./resources/1_164.png)

  BMI 라는 컬럼이 Unknown이라고 뜨네요. 

  **왜 이 부분이 작동하지 않는 걸까요? 이건 SQL 문의 실행원리에 대해 잘 알아야 이해할 수 있습니다. 일단 쉽게 설명드리면 BMI는 우리가 SELECT 절 안에서 설정한 alias입니다. 그런데 BMI 컬럼이 Unknown이라고 뜨는 건 CASE 함수가 실행될 때는 BMI라는 alias가 아직 인식되지 않은 상태라고 봐야 합니다.** 

  하지만 CASE 문에서 매번 이렇게 똑같은, 그리고 긴 표현을 쓰는 건 보기에 안 좋을 것 같은데요. 이 문제를 해결할 수 있는 방법이 있습니다. 

  하지만 그 방법은 우리가 마지막 챕터까지 모두 배워야 이해할 수 있습니다. 

  마지막 토픽까지 열심히 들으시고, [이 문제에 대한 해결책을 설명한 노트](https://www.codeit.kr/learn/3244/)에서 답을 찾아보세요. 