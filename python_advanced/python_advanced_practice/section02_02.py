
print(int)
print(dir(int))
print()
print()

n = 100

print(n+200)
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n.__mul__(100), n*100)


class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('called. >> _ge__ Method')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('called. >> __le__ Method')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('called. sub method')
        return self._height - x._height

s1 = Student('James', 181)
s2 = Student('Mie', 181)

print("TEST")
print(s1>=s2)
print(s1>=s2)
print(s1 - s2)
print(s2 - s1)


# 벡터 (Vector) #numpy
class Vector(object):
  def __init__(self, *args):
    '''Create a vector, example : v = Vector(1,2)'''
    if len(args)==0:
      self._x, self._Y = 0, 0
    else:
      self._x, self._y = args

  def __repr__(self):
    '''Returns the vector information'''
    return 'Vector(%r, %r)' % (self._x, self._y)

  def __add__(self, other):
    '''Returns the vector addtion of self and other'''
    return Vector(self._x+ other._x, self._y+other._y)

  def __mul__(self, other):
    '''Returns the vector multiply of self and other'''
    return Vector(self._x*other._x, self._y*other._y)

  def __bool__(self):
    return bool(max(self._x, self._y))
# Vector Instance 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector(0, 0)

print('EX3-1 - ', v1.__init__.__doc__)
print('EX3-2 - ', v1, v2, v3)
print('EX3-3 - ', Vector.__repr__.__doc__)
print('EX3-4 - ', Vector.__add__.__doc__)
print('EX3-5 - ', v1+v2)
print('EX3-6 - ', Vector.__mul__.__doc__)
print('EX3-7 - ', v1*v2)

# print('EX3-8 - ', v2*10)
print('EX3-9 - ', bool(v1), bool(v2))
print('EX3-10 - ', bool(v3))


print()
print()


