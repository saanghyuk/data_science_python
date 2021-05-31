
print(type(True))
print(type(False))


if False:
  print("No")
else:
  print("Yes2")

a = 10
b = 0
print(a==b)
print(a!=b)


a = 100
b = 60
c = 15

print('and : ', a>b and b>c)
print('or : ', a>b or b>c)

print('ex1 : ', 5 + 10 > 0 and not 7 + 3 ==10) #5+10 먼저, 그 다음에 >나 ==, 그 다음 and not


v1 = 1
while v1 < 11:
    print("v1 is", v1)
    v1+=1

for v2 in range(10):
    print("v2 is:", v2)

for v3 in range(1, 11):
    print("v3 is : ", v3)


numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for n in numbers:
  if n == 33:
    print('Find 33')
    break
  else:
    print("Not Found")
else: #break문을 끝까지 안만나면, 다 시행된 다음에, else문이 시행됨.
  print("Not found 33.....")



#Continue, 이걸 만나면 다음 수행할 곳으로 간다는 것.
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
  if type(v) is float:
    continue
  print(type(v))

