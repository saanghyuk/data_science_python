
class Student():
    """
    Student
    Author : SON
    Date: 2021.05.31
    """
    # class variable
    student_count = 0
    """
    SAMPLE __doc__
    """
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1
    def __str__(self):
        return 'str {}'.format(self._name)
    def __repr__(self):
        return 'str {}'.format(self._name)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count-=1

studt1 = Student('Cho', 2, 3, { 'gender' : 'Male', 'score1' : 65, 'score2':44 })
studt2 = Student('Chang', 2, 3, { 'gender':'Female', 'score1':85, 'score2':74 },'stu2@naver.com')

print(id(studt1))
print(id(studt2))
print(Student.student_count)


a = 'ABC'
b = a
print(a is b) # id를 비교
print(a == b) # 값을 비교


print(studt1==studt2)
print(studt1._name==studt2._name)
print(studt1 is studt2)
print(a is b) # 이러면 True가 나옴.
print(a == b)

print(dir(studt2)) # 함수 확인
print(dir(studt1))
print(studt1.__dict__) # namespace 확인
print(studt2.__dict__)

studt1.detail_info()
studt2.detail_info()


# 비교
# 해당 인스턴스의 class를 알려줌.
# 인스턴스만 보고 얘가 뭔지 모를수가 있잖아.
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) ==  id(studt2.__class__)) #True
print()


studt1._name = 'JUST KIDDING'
studt1.___name = 'JUST KIDDING2'
print(studt1.__dict__)
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)


print()
print()
#클래스 변수는 누구나 접근 가능.
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)
print()
print()


print(Student.__dict__)
print(dir(Student))

del studt2
print(studt1.student_count)
print(Student.student_count)
print(studt2.__dict__)
