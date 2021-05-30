a = {'Name': 'SON', 'Phone':'010-0000-0000', 'birth': 870214}
b = {0: 'Hello, Python', 1: 'Hello, Coding'}
c = {'arr': [1, 2, 3, 4, 5]}


print(a['Name'])
print(a.get('Name'))
print(a.get('address'))
print(c['arr'][1:2])

print(a.keys())
temp = list(a.keys())
print(a.values())
print(1 in b)
print('name' in b)

# Collections
a = set()
b = set([1, 2, 3, 4, 5])
c = set([1, 4, 5, 6, 6])
print(c)
t=tuple(b)
print(t)

s3=set([7, 8, 10, 15])
s3.add(10)
s3.add(7) #중복 허용X

s3.remove(15)
print(s3)
print(type(s3))