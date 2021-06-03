

class VectorP_sample(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))


v_sample = VectorP_sample(20, 40)


class VectorP(object):
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def __iter__(self):
    # 아래 쓴거는 generator야. next호출 하면 x, 그 다음 호출하면 y가 나오라는 뜻.
    # 리스트를 통으로 보낼꺼면 []로 하면 됨.
    return (i for i in (self.__x, self.__y))

  @property
  def x(self):
    print('Called Property X')
    return self.__x

  #getter를 먼저 만들어야 함
  @x.setter
  def x(self, v):
    print('Called Property X Setter')
    self.__x = float(v)

  @property
  def y(self):
    print('Called Property Y')
    return self.__y

  #getter를 먼저 만들어야 함
  @y.setter
  def y(self, v):
    print('Called Property Y Setter')
    if v<30 :
      raise ValueError('30 Below is not possible')
    self.__y = float(v)



# Getter, Setter

v = VectorP(20, 40)
print("===============")
v.__y = 30
print(v.__y)
print("===============")
# print(v.__x) # 접근 불가
print(v.x) # 접근 가능해짐. 우리는 __로 정의했는데, 접근 가능해짐
v.x = 10
print(v.x)

print(v.y)
# v.y = 20 #Error
v.y = 40
print(v.y)

print('EX1-2 -', dir(v), v.__dict__) # ['_VectorP__x', '_VectorP__y', 'x', 'y'] 알아서 이렇게 만들어져 있음.
# dict찍어보면 실제로 변수는 이렇게 저장되어 있는 것을 알 수 있음. 다만, 파이썬에서 자동으로 x로 호출 가능하게 해준거지.
print(v._VectorP__x)
print(v._VectorP__y)
print('EX1-3 - ', v.x, v.y)
# Iter확인. 그대로 돌리면 Generator에서 하나씩 풀리겠지.
for val in v_sample:
  print('EX1-4', val)


# __slot__
# 파이썬 인터프리터에게 통보하는 역할
# 해당 클래스가 가지는 속성을 제한함.
# 파이썬의 모든 인스턴스는 속성을 가지고, __dict__로 dictionary형태로 관리됨.
# 근데 이 dict는 빠른 검색을 위해서  hash값으로관리되기 때문에, 메모리를 많이 잡아먹음.
# 클래스를 100개 1000개 씩 하면, 그 만큼 딕셔너리가 생성되는 것.
# 그래서 slot을 사용해서 __dict__속성 최적화 -> 다수 객체 생성 시 메모리 사용 공간 대폭 감소.
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태 사용.

class TestA(object):
  __slots__=('a')

class TestB(object):
  pass

use_slot=TestA()
no_slot=TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__) dictionary 안써서 에러 남.
print('EX2-1 -', no_slot)
print('EX2-2 -', no_slot.__dict__)

import timeit
#측정을 위한 함수 선언
def repeat_outer(obj):
  # 얘도 클로저야 obj.a가 밖에서 계속 저장되겠지.
  def repeat_inner():
    obj.a = 'Test'
    del obj.a

  return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=100000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=100000)))




# 객체 슬라이싱
class Objects:
  def __init__(self):
    self._numbers = [n for n in range(1, 10000, 3)]

  # 파이썬에에 있는 len을 오버라이딩
  def __len__(self):
    return len(self._numbers)

  def __getitem__(self, idx):
    return self._numbers[idx]

s = Objects()
# print('EX3-1- ', s.__dict__)
print('EX3-2 - ', len(s)) # 위에서 __len__을 안해놨으면 error가 남. 실제로 확인해보면 len이 없어.

# 파이썬의 list class를 까보면 실제로 __len__과 __getitem__이 저렇게 되어 있음.
# 리스트에서 제공하는 것들중 두가지를 오바리이딩 했기 때문에, 이제부터 s[:100], s[3]이런게 가능한 거임.
print('EX3-3 -  ', len(s._numbers)) # 이렇게 했어야겠지.
print('EX3-4 - ', s[:100])
print('EX3-5 - ', s[-1])
print('EX3-6 - ', s[::10])

print()
print()


class IterTestA():
  def __getitem__(self, idx):
    return range(1, 50, 2)[idx]  # range(1, 50, 2)


i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4])  # [idx] 제거 후
print('EX4-3 -', 3 in i1[1:10])  # contain을 파이썬이 알아서 만든 것.
# print('EX4-4 -', [i for i in i1[:]]) # iter을 파이썬이 알아서 만든 것.
# print('EX4-5 - ', len(i1) ) # 자동으로 안만들어 주네.

print()
print()




from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

    def __len__(self, idx):
      return len(range(1, 50, 2)[idx])
i2 = IterTestB() # TypeError: Can't instantiate abstract class IterTestB with abstract methods __len__

print('EX4-5 -', i2[4])
print('EX4-6 -', i2[4:10]) # [idx] 제거 후
print('EX4-7 -', 3 in i2[1:10]) # contain을 파이썬이 알아서 만든 것.
print('EX4-8 -')
print()
print()
