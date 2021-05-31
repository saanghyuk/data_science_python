BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'SON','sh@naver.com','010-3030-2030','kormat.co.kr','2021-03-12 17:45:29');
INSERT INTO "users" VALUES(2,'Yoon','syoon@gmail.com','010-6391-4103','Yoon.com','2021-03-12 17:45:29');
INSERT INTO "users" VALUES(3,'SON','sh@naver.com','010-3030-2030','kormat.co.kr','2021-05-31 15:52:29');
INSERT INTO "users" VALUES(4,'Yoon','syoon@gmail.com','010-6391-4103','Yoon.com','2021-05-31 15:52:29');
COMMIT;
