



t = 'ABCDEF'
# for
for c in t:
  print('EX1-1 - ', c)


print()

# While 사용
w = iter(t)
while True:
  try:
    print('EX1-1 - ', next(w))
  except StopIteration as log:
    print(log)
    break


# collections
from collections import abc
# 반복형(Iter) 확인 가능
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))
print('EX1-4 -', dir(iter(t)))
print('EX1-4 _1 - ', dir(t)) # __iter__가 나오면 반복 가능하다는 것.

print()
print()



class WordSplitIter:
  def __init__(self, text):
    self._idx = 0
    self._text = text.split(' ')

  def __next__(self): # Iterator(next) 처럼 만들기
    print('Called __next__')
    try:
      word = self._text[self._idx]
    except IndexError:
      raise StopIteration('Stop!! Stop!!')

    self._idx += 1
    return word

  def __iter__(self): # Iterable(for) 만들기
    print('Called __iter__')
    return self

  def __repr__(self):
    return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')
for i in wi:
    print(i)
print(wi._idx)
print(type(wi))





class WordSplitGenerator:
  def __init__(self, text):
    self._text = text.split(' ')

  def __iter__(self):
    for word in self._text:
      yield word #  Generator, 이게 next에서 코드 썻던거 다 해주는 거야.
    return

  def __repr__(self):
    return 'WordGenerator(%s)' % (self._text)



wg = WordSplitGenerator('Who says the nights are for sleeping')
print(type(wg))
print(dir(wg))

wt= iter(wg) # iter가 없으면, 애초에
print(dir(wt))
print(type(wt)) # Generator로 바뀜

for i in wg:
    print(i)
for i in wt:
    print(i)

print("=====================")
# ('EX3-1- ', wg)
# print('EX3-2- ', next(wg))
# print('EX3-3- ', next(wg))
# print('EX3-4- ', next(wg))
print("=====================")

def generator_ex1():
  print('start')
  yield 'AAA'
  print('continue')
  yield 'BBB'
  print('end')

# temp = iter(generator_ex1())
print(type(generator_ex1()))
print('EX4-1 - ', next(generator_ex1()))
# print('EX4-1 - ', next(temp))
# print('EX4-1 - ', next(temp))

import itertools


# 조건
gen2 = itertools.takewhile(lambda n : n<1000, itertools.count(1, 2.5))

for v in gen2:
  print('EX6-5 - ', v)

print()
print()


# 필터 반대
# 해당 조건을 제외한 나머지들이 나오게 됨.
gen3 = itertools.filterfalse(lambda n : n<3, [1, 2, 3, 4, 5])
for i in gen3:
  print('EX6-6 - ', i)

print()
print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
  print('EX 6-7 - ', v)

print()
print()

# 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print('EX6-8', list(gen5))

# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
for i, v  in enumerate('ABCDE'):
  print(i, v)
print('EX6-9', list(gen6))

print()
print()

# 개별
gen7 = itertools.product('ABCDE')
print('EX6-10', list(gen7)) #[('A',), ('B',), ('C',), ('D',), ('E',)]
# for i in gen7:
#   print(i)

print()
print()


# 연산(경우의 수) 2면 2개 1쌍, 3이면 3개가 1쌍
gen8 = itertools.product('ABCDE', repeat = 2 )
print('EX6-12', list(gen8))

print()
print()


# 그룹화
gen9 = itertools.groupby('AAAABBBCCCCDDEEEE')
#print('EX6-12', list(gen9))
for chr, group in gen9:
  print('EX6 - 12 - ', chr, ':', list(group))

