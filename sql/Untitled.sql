SELECT email,  CONCAT(height, 'cm', ', ', weight, 'kg') AS '키와 몸무게',  
	weight / ( (height/100) * (height/100) ) AS BMI FROM copang_main.member;
