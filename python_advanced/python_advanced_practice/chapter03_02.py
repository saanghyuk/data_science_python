t1 = (10, 20, (30, 40, 50))
t2 = [10, 20, [30, 40, 50]]

print('EX1-2 - ', hash(t1))

print()
print()

import csv

source =(
  ('k1', 'val1'),
  ('k1', 'val2'),
  ('k2', 'val3'),
  ('k2', 'val4'),
  ('k2', 'val5')
)
new_dict1 = {}
new_dict2 = {}

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# USE SetDefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
    print(new_dict2)
print(new_dict2)


print(dir(dict))




from types import MappingProxyType
d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)
print('EX5-1 - ', d, id(d))
print('EX5-2 - ', d_frozen, id(d_frozen))
# is는 id비교, ==는 값 비교
print('EX5-3 - ', d is d_frozen, d == d_frozen)


s1 = {'Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'])
s3 = {3}
s4 = {} #이렇게 놓으면 공집합이 아니라 딕셔너리
s4_1 = set() # 이게 공집합
s5 = frozenset({'Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'})
# print(id(s5))

s1.add('Melon')
print('EX6-1 -', s1, type(s1))

print('EX6-1 -', s1, type(s1))
print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))




# 선언 최적화
print('EX6-5 - ')
a = {5}
b = set([10])
from dis import dis
print(dis('{10}')) # 이렇게 선언하는게 더 빠르다는 것.
  # 1           0 LOAD_CONST               0 (10)
  #             2 BUILD_SET                1
  #             4 RETURN_VALUE
print('EX6-6 - ')
print(dis('set([10])'))
  # 1           0 LOAD_NAME                0 (set)
  #             2 LOAD_CONST               0 (10)
  #             4 BUILD_LIST               1
  #             6 CALL_FUNCTION            1
  #             8 RETURN_VALUE

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name
print('EX7-1 - ')
print({chr(i) for i in range(0, 256)}) #0부터 255까지의 유니코드 데이터
print({name(chr(i), '') for i in range(0, 256)}) #0부터 255까지의 유니코드 데이터 설명
print()
print()

