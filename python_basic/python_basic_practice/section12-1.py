
import sqlite3
import datetime

now = datetime.datetime.now()
print(now)
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowDatetime)
print('nowDatetime : ', nowDatetime)

print(sqlite3.version)
print(sqlite3.sqlite_version)


conn = sqlite3.connect('../resource/database.db', isolation_level=None) #auto commit
c = conn.cursor()
print('Cursor Type : ', type(c))
c.execute("INSERT INTO users VALUES(3, 'SON', 'sh@naver.com', '010-3030-2030', 'kormat.co.kr', ? )", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (4, 'Yoon', 'syoon@gmail.com', '010-6391-4103', 'Yoon.com', nowDatetime ))
c.execute("SELECT * FROM users")
conn.close()