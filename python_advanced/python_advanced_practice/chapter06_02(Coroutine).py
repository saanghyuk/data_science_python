
# 코루틴 예제
def coroutine1():
  print('>>> coroutine started')
  i = yield
  print('>>> coroutine received : {}'.format(i))

# Generator 선언
c1 = coroutine1()
print('EX1-1 - ', c1, type(c1)) # GENERATOR

# yield 실행 전까지 진행

next(c1) # 임시 주석
# next(c1)
#
# c2 = coroutine1()
# next(c2)
# c2.send(200)



def coroutine2(x):
  print('>>>>Coroutine Started : {}'.format(x))
  # a = yield
  # print(a)
  y = yield x # y는 메인루틴에서 받을 값, x는 메인루틴으로 전달할 값.
  print('>>>>Coroutine Received : {}'.format(y))
  z = yield x+y
  print('>>>>Coroutine Received : {}'.format(z))

c3 = coroutine2(10)
from inspect import getgeneratorstate

print('EX1-2,', getgeneratorstate(c3)) #GEN_CREATED
print("TEST1", next(c3)) # send는 대기상태이고, 보낼꺼는 이미 보낸 상태가 됨. 10이 나옴.
print('EX1-3,', getgeneratorstate(c3)) #GEN_SUSPENDED
print("TEST2", c3.send(15))
print('EX1-4,', getgeneratorstate(c3)) #GEN_SUSPENDED
# print(c3.send(20)) # 예외처리 해야함.

print()
print()



# 데코레이터 패턴
from functools import wraps

def coroutine(func):
  '''Decorator run until yield'''
  @wraps(func) # 주석이나 모든 것까지 다 가지고 가겠다는 데코레이터
  def primer(*args, **kwargs):
    gen = func(*args, **kwargs)
    print(next(gen)) # next 한번 호출하고 보내는 것
    return gen
  return primer

@coroutine
def summer():
  total = 0
  term = 0
  while True:
    term = yield total
    total += term

# Coroutine은 이렇게 담아야 generator로 바뀜. 그냥 하면, generator가 안됨.
su = summer() #이렇게 담기는 순간 클로져가 있으니깐, 내부 prime이 실행된 상태로 return을 받겠지.
# print('EX2-0 - ', next(su))
print(getgeneratorstate(su))
print('EX2-1 - ', su.send(100))
print(getgeneratorstate(su))
print('EX2-2 - ', su.send(40))
print(getgeneratorstate(su))
print('EX2-3 - ', su.send(60))
print(getgeneratorstate(su))
print()
print()


