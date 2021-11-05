USE coupang_main;
SELECT * FROM member WHERE email = "taehos@hamil.net";
SELECT * FROM member WHERE age>27;
SELECT * FROM member WHERE age BETWEEN 30 AND 39;
SELECT * FROM member WHERE age NOT BETWEEN 30 AND 39;
SELECT * FROM member WHERE sign_up_day > '2019-01-01';
SELECT * FROM member WHERE sign_up_day BETWEEN  '2018-01-01' AND '2018-12-31';
SELECT * FROM member WHERE address LIKE '서울%';
SELECT * FROM member WHERE age IN (20, 30);
SELECT * FROM member WHERE email LIKE 'c_____%';
SELECT * FROM member WHERE address NOT LIKE '%호';

# DATE
SELECT * FROM member WHERE DAYOFMONTH(sign_up_day) BETWEEN 15 AND 30;
SELECT email, sign_up_day, DATEDIFF(sign_up_day, '2019-01-01') FROM member;
SELECT email, sign_up_day, DATEDIFF(sign_up_day,CURDATE()) FROM member;
SELECT email, sign_up_day, DATE_ADD(sign_up_day, INTERVAL 300 DAY) FROM member;
SELECT email, sign_up_day, DATE_SUB(sign_up_day, INTERVAL 300 DAY) FROM member;
SELECT email, sign_up_day,UNIX_TIMESTAMP(sign_up_day) FROM member;

SELECT * FROM member  ORDER BY height ASC LIMIT 0, 10;

SELECT COUNT(email) FROM member;
SELECT MAX(height) FROM member;
SELECT MIN(height) FROM member;
SELECT AVG(height) FROM member;

SELECT SUM(height) FROM member;
SELECT ABS(height) FROM member;
SELECT SQRT(height) FROM member;
SELECT CEIL(height) FROM member;
SELECT FLOOR(height) FROM member;
SELECT ROUND(height) FROM member;

# NULL
SELECT * FROM member WHERE address IS NULL;
SELECT * FROM member WHERE address IS NOT NULL;

# NULL을 SUBSTITUDE
SELECT 
	COALESCE(height, '####'),
    COALESCE(weight, '----'),
    COALESCE(height, '@@@')
FROM member ;

# NULL이면 weight*2.3, weight도 NULL이면 'N/A'
SELECT COALESCE(height, weight*2.3, 'N/A') FROM member;

# IFNULL :  height가 null이면, 'N/A'를 쓴다. 
SELECT IFNULL(height, 'N/A') FROM member;

# IF  height가 not null이면 height, 아니면 N/A
SELECT IF(height IS NOT NULL, height, 'N/A') FROM member;

# CASE
SELECT
	CASE
		WHEN height IS NOT NULL THEN height
        ELSE 'N/A'
	END
FROM member;


# 이상한 값 제외
SELECT AVG(age) FROM member;
SELECT * FROM member WHERE age BETWEEN 5 AND 100;
SELECT AVG(age) FROM member WHERE age BETWEEN 5 AND 100;
 
 
 # 컬럼끼리 계산하기
 SELECT email, height, weight ,  weight / ( (height/100) * (height/100) ) AS BMI FROM member;
 
 # CONCAT
 SELECT email, CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
weight / ( (height/100) * (height/100) ) AS BMI FROM member;
# 컬럼 변환
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
FROM member
ORDER BY obesity_check;


# 고윳값
SELECT DISTINCT(gender) FROM member;
SELECT DISTINCT(SUBSTRING(address, 1, 2)) FROM member;
SELECT COUNT(DISTINCT(SUBSTRING(address, 1, 2))) FROM member;


# 문자열 관련 함수
# LENGTH
SELECT *, LENGTH(address) FROM member;
# UPPER, LOWER
SELECT *, UPPER(email) FROM member;
SELECT *, LOWER(email) FROM member;

# LPAD, RPAD
 #LPAD(age, 10, ’0’)는 age 컬럼의 값을, 왼쪽에 문자 0을 붙여서 총 10자리로 만드는 함수입니다. 
 # 보통 어떤 숫자의 자릿수를 맞출 때 자주 사용하는 함수입니다. 아래 그림을 보면 무슨 뜻인지 바로 이해할 수 있습니다.
 
# GROUPING
SELECT gender, COUNT(*), AVG(height) FROM member GROUP BY gender;
SELECT MIN(weight) FROM member GROUP BY gender;

SELECT 
	SUBSTRING(address, 1, 2)  as region,
    COUNT(*)
FROM member 
GROUP BY SUBSTRING(address, 1, 2);

SELECT 
	SUBSTRING(address, 1, 2)  as region,
  gender,
  COUNT(*)
FROM member 
GROUP BY 
	SUBSTRING(address, 1, 2), 
  gender
HAVING region ='서울';


SELECT 
gender,
	SUBSTRING(address, 1, 2)  as region,
    
    COUNT(*)
FROM member 
GROUP BY 
gender, 
	SUBSTRING(address, 1, 2)
WITH ROLLUP
HAVING 
	region IS NOT NULL 
ORDER BY 
	region ASC, 
    gender DESC;
    
SELECT SUBSTRING(address, 1, 2) as region, gender, COUNT(*)
FROM member
GROUP BY SUBSTRING(address, 1, 2), gender WITH ROLLUP
ORDER BY region ASC, gender DESC;


SELECT 
		item.id,
    item.name,
    stock.item_id,
    stock.inventory_count
FROM item LEFT OUTER JOIN stock
ON item.id = stock.item_id;
 
 SELECT 
	MAX(copang_report.price) 
	AS max_price, AVG(copang_report.star) AS avg_star, 	
	COUNT(DISTINCT(copang_report.email)) AS distinct_email_count 
FROM 
(SELECT price, star, email FROM item AS i INNER JOIN review AS r ON r.item_id = i.id 
INNER JOIN member AS m ON r.mem_id = m.id) AS copang_report;

SELECT 
	id, 
	name, 
  price,
 	(SELECT MAX(price) FROM item) AS 'MAX PRICE'
FROM item;


SELECT * FROM item
WHERE id IN 
(
SELECT item_id
FROM review
GROUP BY item_id HAVING COUNT(*) >= 3
);

SELECT 
	AVG(review_count)
FROM 
(SELECT 
	SUBSTRING(address, 1, 2) AS region, 
    COUNT(*) AS review_count
FROM review AS r LEFT OUTER JOIN member AS m
ON r.mem_id = m.id 
GROUP BY SUBSTRING(address, 1, 2)
HAVING region IS NOT NULL
	AND region != '안드');
    
SELECT 
	SUBSTRING(address, 1, 2) AS region, 
    COUNT(*) AS review_count
FROM review AS r LEFT OUTER JOIN member AS m
ON r.mem_id = m.id 
GROUP BY SUBSTRING(address, 1, 2)
HAVING region IS NOT NULL
	AND region != '안드';