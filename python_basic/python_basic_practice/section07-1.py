
class UserInfo:
    def __init__(self, name):
        self.name = name
        print("클래스 초기화 : ", name)
    def user_info_p(self, dish):
      print('Name : ', self.name)
      print('Favorite Food : ', dish)

user1 = UserInfo("손상혁")
user1.user_info_p('쿠키')
user2 = UserInfo("Yoon")
user2.user_info_p("Pizza")
print("__dict__")
print(user1.__dict__)
print(user2.__dict__)


class SelfTest:
    def function1():
        print("function1 called")
    def function2(self):
        print(id(self))
        print("function2 called")

self_test = SelfTest()
SelfTest.function1()


print(id(self_test))
self_test.function2() #같음
print(id(SelfTest))


class WareHouse:
  stock_num = 0
  def num_check():
      print("num is ", WareHouse.stock_num)
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num+=1 #Class변수는 Class변수대로 카운팅 되고 있네
  def __del__(self): #인스턴스 종료될때 호출되는 Method
    WareHouse.stock_num-=1

user1= WareHouse('Kim')
user2 = WareHouse('Son')
user3 = WareHouse('Yoon')

print(user1.__dict__) #Self의 변수들이 나옴.
print(user2.__dict__)
print(user3.__dict__)

# Class Name Space
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)
print(WareHouse.num_check())
