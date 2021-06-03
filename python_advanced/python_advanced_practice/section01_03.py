

class Student(object):
    '''
    Student Class
    Author : SON
    Date : 2021.03.14
    Description: Class, Static, Instance Method
    '''
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    def get_fee(self):
        return 'Before Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Instance Method
    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)

    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.tuition_per = per
        print("Succeed! Tuition Increased!")

    @classmethod
    # 지금까지는 instnace = Student(a, b, c, d) 이런 방식으로 했지만,
    # 파이썬에서는 아래와 같은 생성자를 classmethod로 만들기를 권고함
    # instance = Student.student_const() 이렇게
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    # 유연하고 편함. 클래스 안에, 관련된 함수를 같이 넣어 놓음.
    # cls와 self 둘 다 필요가 없음.
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'



#학생 인스턴스
student_1 = Student.student_const(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student.student_const(1, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)


print(student_1)
print(student_2)
print(student_1.__dict__)
print(student_2.__dict__)


#전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(인상 전)
print(student_1.get_fee())
print(student_2.get_fee())
print()

# 학비 인상(클래스 메소드 미사용)
# 직접 접근하는 것? 너무 안좋다고 말했음.
# 실수로 1.2대신 1.3누르면 어쩔꺼야.
Student.tuition_per = 1.2
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()
Student.tuition_per = 1.0 # reset용 code

Student.raise_fee(0.9)
Student.raise_fee(1)
Student.raise_fee(1.2)


# class method로 생성자 만들어 놓기
# @classmethod
# def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
#   return cls(id, first_name, last_name, email, grade, tuition*cls.tuition_per, gpa)
#클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Lee', 'Miyoung', 'student4@gmail.com', '4', 600, 4.1)
print(student_4.tuition_per)


print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))