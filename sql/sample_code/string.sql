SELECT DISTINCT(SUBSTRING(address, 1, 2)) FROM copang_main.member;
SELECT COUNT(DISTINCT(SUBSTRING(address, 1, 2))) FROM copang_main.member;
SELECT LENGTH(address) FROM copang_main.member;
SELECT UPPER(address) FROM copang_main.member;
SELECT LOWER(address) FROM copang_main.member;
SELECT RPAD(gender, 10, 'a') FROM copang_main.member;