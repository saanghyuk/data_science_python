
print(dir())

x = {'name':'kim', 'age':33, 'city': 'Seoul'}
y = x

print(id(x), id(y))
print(x==y)
print(x is y)
print(x, y)

x['class'] = 10
print(x)
print(y)


tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])
print('EX3-1 -', id(tuple1), id(tuple2)) # 당연히 id는 다르지
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))
print('EX3-5', tuple1[2] is tuple2[2]) # 내부 리스트의 id값도 다름.

print()
print()




#copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)
print(id(tl1))
print(id(tl2))
print(id(tl3)) # 얘만 id값 다름.

print('EX4-1', tl1 == tl2) # True
print('EX4-2', tl1 is tl2) # True
print('EX4-1', tl1 == tl3) # True
print('EX4-2', tl1 is tl3) # False, list객체 생성자만 넣었는데 id가 다르네.
# 즉 생성자를 넣어줘야 안전하다는 것.
print(id(tl1[1]), id(tl1[2]))
print(id(tl2[1]), id(tl2[2]))
print(id(tl3[1]), id(tl3[2]))
tl1[1][0] = 200
print(tl1)
print(tl2)
print(tl3)


tl1[1]+=[110, 120]
tl1[2]+=(110, 120)

print(tl1)
print(tl3)
print("==========================")
import copy
print(tl1)
tl2 = copy.copy(tl1)
tl3= copy.deepcopy(tl1)
print(tl2)
print(tl3)
tl1[1][0]= 50
print(tl1)
print(tl2)
print(tl3)



print("===========================")

class Basket:
  def __init__(self, products=None):
    if products is None:
      self._products = []
    else:
      self._products=list(products) # 아이디 새로 할당하는 것.

  def put_prod(self, prod_name):
    self._products.append(prod_name)

  def del_prod(self, prod_name):
    self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)
print('EX5-1 -', id(basket1), id(basket2), id(basket3)) # 객체 복사하니깐 copy든 deep copy든 다 id가 다르게 나옴.
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products)) #얘는 1, 2가 똑같이 나오고 3은 다름.
# 즉 얕은 copy는 객체는 다르게 복사된것 같아도 내부의 attribute들이 똑같이 복사가 된거야.
# deep copy는 내부 attributes까지 다르게 복사되는 것.
# deep copy는 끝까지 쫓아가서 깊게 복사하는 것.


print()
basket1.put_prod('Oranage')
basket2.del_prod('Snack')
print('EX5-3 -', basket1._products) # 똑같이 변경해버렸음.
print('EX5-4 -', basket2._products) # 똑같이 변경해버렸음.
print('EX5-5 -', basket3._products)


# 결론 복사가 되는 것 같아도 대부분은 얕은 복사라서 외면만 복사되고, 내부는 복사가 안된다.
# 진짜 바뀌면 안되는 거면 deep_copy를 떠라.


def mul(x, y):
  x += y
  return x

x=5
y=10
# x랑 y가 함수에 들어갔다가 나와도 당연히 x, y 는 원본이 유지됨.
print('EX6-1 - ', mul(x, y), x, y)

a = [10, 100]
b = [5, 10]

print('EX6-2 ', mul(a, b), a, b)
print(a)
print(b)


tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1) # 이렇게 하면 원래는 id값이 바뀌는데 안바뀌고 참조를 반환하네.
tt3 = tt1[:]


print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2)) # True, id값 같음
print('EX7-2 - ', tt1 is tt3, id(tt1), id(tt3)) # True, id값 같음



tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 - ', tt4 is tt5, tt4==tt5, id(tt4), id(tt5)) # 얘는 id 다름.
print('EX7-4 - ', ss1 is ss2, ss1==ss2, id(ss1), id(ss2)) #얘는 all true

print(id('a'), id('a'))