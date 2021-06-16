from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다 : 자식 클래스가 오버라이딩 할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다 : 자식 클래스가 오버라이딩 할 것"""
        pass

class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2*self.width +2*self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)

class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 너비를 나타낸다"""
        return pi*self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2*pi*self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)

class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)

class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3*self.side

class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다. ")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합ㅇ을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판에 안에 있는 도형들: \n\n"
        for shape in self.shapes:
            res_str+= str(shape)+"\n"
        return res_str



triangle = EquilateralTriangle(4)
paint_program = Paint()
paint_program.add_shape(triangle)
print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())




# cylinder = Cylinder(7, 4)
# rectangle = Rectangle(3, 7)
# circle = Circle(4)
#
# paint_program = Paint()
# paint_program.add_shape(rectangle)
# paint_program.add_shape(circle)
# paint_program.add_shape(cylinder)
#
# print(paint_program.total_area_of_shapes())
# print(paint_program.total_perimeter_of_shapes())
