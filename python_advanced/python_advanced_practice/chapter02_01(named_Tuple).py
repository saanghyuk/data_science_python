
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_leng1 = sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
print(line_leng1)


from collections import namedtuple
Point = namedtuple('Point', 'x y')
print("--------------")
print(Point.__dict__)
print("--------------")
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_leng2 = sqrt((pt2.x-pt1.x)**2 + (pt2.y-pt1.y)**2)
print('EX1-2', line_leng2)
print('EX1-2', line_leng1 ==line_leng2)


# 띄어쓰기 이외에도 리스트로 넣어도 됨.
Point0 = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# class 는 예약어이고, 중복은 안됨

# rename을 True로 하면, 중복에 대해서 에러를 터뜨리지 않고, 다른 이름을 자동으로 생성해줌
# Point 4 에서는 x의 중복과 예약어 class문제를 rename이 해결해 주는 것.
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False
print('EX2-1 -', Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
print('EX2-2', p1, p2, p3, p4)
print(p4)

# Dict To Unpacking
temp_dict = {'x': 75, 'y': 55}
p5 = Point(**temp_dict)
print(p5)


print()
print()

print(p1)
print(p1[0]+p1[1])
print(p1.x + p1.y)

# Rename
print('EX3-4 - ', p4)

#네임드 튜플 메소드
temp = [52, 38]

# _make(): 새로운 객체를 생성
# list to named tuple
p4 = Point1._make(temp)
print('EX4-1-', p4)



# _fields : 필드네임확인
print('EX4-2-', p1._fields, p2._fields, p3._fields)



# _asdict():  OrderedDict로 반환
print('EX4-2 - ', type(p1._asdict()), p4._asdict())
print(type(dict(p1._asdict())))

# _replace() 근데 튜플은 불변이라서 새로운 수정된 객체를 반환(id값이 달라짐)
print(p2)
print('EX4-4 - ', p2._replace(y=100))
print(id(p2))
print(id(p2._replace(y=100)))
print()
print()


Classes = namedtuple('Classes', ['rank', 'number'])
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print(ranks, numbers)
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(students)
print(len(students))
print(students)
print(students[4].rank)
