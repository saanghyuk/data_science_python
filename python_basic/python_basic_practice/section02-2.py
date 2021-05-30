import sys

# 파이썬 기본 인코딩
# 파이썬은 기본 utf-8
print(sys.stdin.encoding)
print(sys.stdout.encoding)

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j )




# Class
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
