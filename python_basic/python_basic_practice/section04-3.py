

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 20, 'Pen', 'Banana', 'Orange']
e = [10, 20, 'Pen', 'Banana', 'Orange', ['Apple', 'Banana']]

print(d[3])
print(d[-1] + d[-2])
print(e[-1][-1])

print(d[0:3])
print(d[0:1])
print(e[-1][0:2])

print(c+d)
print(c*3)
print(str(c[0])+'hi')

#C에서 [1:2]하면 [1]이 남잖아. 그 구간을 아래 3개로 대체하는 거지.
c[1:2]=[100, 1000, 10000]
print(c)
#아래처럼 하나를 쓰고 리스트를 넣으면 nested가 됨.
c[1] = ['a', 'b', 'c']
print(c)

del(c[1])
print(c)

y= [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.reverse()
print(y)

y.insert(2, 7)
print(y)
y.remove(2)
print(y)

y.pop()
print(y)

ex= [88, 77]
y.extend(ex)
print(y)

y.append(ex)
print("================")
print(y)
print(y.index(88))
print(y.count(88))
print("================")

a = ()
b = (1,)#마지막은 컴마로 끝내기
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
# error del c[2]
print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])



z = (5, 2, 1, 3, 4, 3)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(3))
