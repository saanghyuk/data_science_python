
chars = "!@#!@%@#%!#%"
codes1 = []
for s in chars:
    codes1.append(ord(s))
    print(ord(s))
print('EX1-1 - ', codes1)

codes2 = [ord(s) for s in chars]
print(codes2)

codes3 = [ord(s) for s in chars if ord(s) > 40]

codes4 =list(filter(lambda x : x>40, map(ord, chars)))

# Generator
import array
tuple_g = (ord(s) for s in chars)
print('EX2-1 - ', tuple_g)

print('EX2-2 ', next(tuple_g))
print('EX2-3 ', next(tuple_g))
print('EX2-3_1 ', next(tuple_g))

# array는 첫번째 자료형을 알려줌. int
array_g = array.array('I', (ord(s) for s in chars))
print('EX2-4 - ', array_g)
print('2-5.', array_g.tolist())


print('3-1. ', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))
print('3-2. ', ['%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)])

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
  print('3-3. ', s)



# LIST 사용 시 주의할 점
# LIST에서 *를 쓴다는 것은 복제를 의미하는 것.
marks1 = [['~']*3 for n in range(3)]
marks2 = [['~']*3]*3
print(marks1)
print(marks2)
marks1[0][1]='X'
marks2[0][1]='X' #모든 리스트의 두번째 인덱스가 다 바뀜.
print(marks1)
print(marks2)
print(id(marks1[0][0]), id(marks1[0][2]))
print(id(marks1[0]), id(marks1[1]))
print(id(marks2[0]), id(marks2[1]))
print(id(marks2[0][0]), id(marks2[0][2]))

print('4-5. ', [id(i) for i in marks1])
print('4-6. ', [id(i) for i in marks2])

a= ['asdf']*3
print([id(b) for b in a])
a[2] = 1
print(a)
list1 = [[1, 2, 3] for i in range(3)]
list2 = [[1, 2, 3]]*3

for i in list1:
    print(id(i))
for i in list2:
    print(id(i))
print(list1)
print(list2)
list2[2][1] = [1, 5, 6]
print(list2)

#Tuple Packing
print('5-1 - ', divmod(100, 9))
print('5-2 - ', *divmod(100, 9))
print('5-3 - ', *(divmod(100, 9)))

x, y, *rest = range(10)
print(x, y, rest)


l = (10, 15, 20)
m = [10, 15, 20]

print('6-1 - ', l, m, id(l), id(m))

l *= 2
m *= 2
print('EX6-3', l, m, id(l), id(m))


f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print(sorted(f_list))
print(sorted(f_list, key=len))
print('EX-7 - 4', sorted(f_list, reverse=True, key=lambda x:x[-1]))

a = f_list.sort()
print(a, f_list)
print('EX7-7 - 7', f_list.sort(reverse=True), f_list)
print('EX7-7 - 8', f_list.sort(key=len), f_list)
print('EX7-7 - 9', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)
