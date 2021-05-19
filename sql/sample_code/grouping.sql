SELECT 
	SUBSTRING(address, 1, 2)  as region,
    gender,
    COUNT(*) 
FROM copang_main.member 
GROUP BY 
	SUBSTRING(address, 1, 2), 
    gender
WITH ROLLUP
HAVING 
	region IS NOT NULL 
ORDER BY 
	region ASC, 
    gender DESC;