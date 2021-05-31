
class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type=type
        self.color=color

    def show(self):
        return "This Car\'s Class \'Show Method!\'"


class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
        print("Your Car Name : %s" % self.car_name)

    def show_model(self):
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
  """Sub Class"""
  def __init__(self, car_name, type, color):
      super().__init__(type, color) #부모한테 넘겨주기
      self.car_name = car_name
  def show_model(self):
      return "Your Car Name: %s" % self.car_name
  def show(self): #Overriding, 부모한테 있는 메소드를 써놓으면 덮어쓰기가 되는 것.
      print(self.type)
      print(super().show()) #부모에 있던거 한번 호출 하고.
      return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)


model1 = BmwCar('520d','sedan', 'red')
print(model1.color)
print(model1.type)
print(model1.car_name)
model1.show()
print(model1.show_model())
print(model1.__dict__)

model2 = BenzCar('220d', 'suv', 'Black')
print(model2.show())



#Inheritance
print(BmwCar.mro()) #왼쪽에서 오른쪽 방향으로 보면 되.
print(BenzCar.mro()) #왼쪽에서 오른쪽 방향으로 보면 되.


#예제2
#다중 상속
class X(object): #모든 클래스는 object class를 상속
  pass

class Y():
  pass

class Z():
  pass

class A(X, Y): #A는 X와 Y 상속
  pass

class B(Y, Z): #B는 Y와 Z 상속
  pass

class M(B, A, Z): #B는 Y와 Z 상속
  pass

print(M.mro())

#상속은 언제나 앞에 있는 것부터 영향을 받음.

