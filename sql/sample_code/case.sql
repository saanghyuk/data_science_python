SELECT email, 
CONCAT(height, 'cm', ', ', 'weight', 'kg') AS '키와 몸무게',
weight / ( (height/100) * (height/100) ) AS BMI,

CASE age
	WHEN 29 THEN '스물 아홉 살'
    WHEN 30 THEN '서른 살'
    ELSE age
END, 

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
