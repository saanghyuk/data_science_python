# Liskov Substitution Principle

- #### 리스포크 치환 원칙 이해하기

  ![5_14](./resources/5_14.png)

  이 원칙의 의미는, 

  **부모 클래스의 인스턴스를 사용하는 위치에, 자식 클래스의 인스턴스를 대신 사용했을 떄, 코드가 원래 의도대로 작동ㅇ해야 한다는 것. **

  ![5_14](./resources/5_15.png)

  자식 클래스의 인스턴스는, 부모 클래스의 인스턴스 이기도 함. 

  ![5_14](./resources/5_16.png)

  이런 성질 떄문에, 부모 클래스의 인스턴스가 들어갈 자리에, 자식 클래스의 인스턴스를 넣을 수도 있음. 

  리스코프 치환원칙은, 자식 클래스의 인스턴스가 부모 클래스의 인스턴스가 행동하는 범위 내에서 행동해야 한다는 원칙. 

  **즉, 부모클래스의 행동규약을 자식클래스가 위반하지 말것.** 

  ![5_14](./resources/5_17.png)

  그런데, 부모클래스의 행동 규약을 자식클래스가 어긴다는 것이 무슨 말이지? 자식 클래스가 부모클래스의 변수와 메소드를 물려받기만 한다면, 부모 클래스의 행동규약을 어길 일이 없음. 

  ![5_14](./resources/5_18.png)

  그런데 오버라이딩 한다면 또 얘기가 달라짐. 

  ![5_14](./resources/5_19.png)

  이 오버라이딩을 할때, *잘못하면 리스코프 치환 원칙을 어길 수가 있음.*

  ![5_14](./resources/5_20.png)

  이렇게 오버라이딩 잘못하는 경우는 크게 2가지 경우가 있음. 

  ![5_14](./resources/5_21.png)

  이번에는 첫번째 경우 먼저 보자.

  ```python
  class Employee:
      """직원 클래스"""
      company_name = "코드잇 버거"
      raise_percentage = 1.03
  
      def __init__(self, name, wage):
          self.name = name
          self._wage = wage
  
      def raise_pay(self):
          """직원 시급을 인상하는 메소드"""
          self._wage *= self.raise_percentage
  
      @property
      def wage(self):
          return self._wage
  
      def __str__(self):
          """직원 정보를 문자열로 리턴하는 메소드"""
          return Employee.company_name + " 직원: " + self.name
  
  
  class Cashier(Employee):
      """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
      burger_price = 4000
  
      def __init__(self, name, wage, number_sold=0):
          super().__init__(name, wage)
          self.number_sold = number_sold
  
      def raise_pay(self, raise_amount):
          """직원 시급을 인상하는 메소드"""
          self.wage += self.raise_amount
  
      @property
      def wage(self):
          return "시급 정보를 알려줄 수 없습니다"
  
  ```

  ```python
  employee_1 = Employee("손상혁", 7000)
  employee_2 = Employee("이미영", 9500)
  
  cashier_1 = Cashier("김대위", 9000)
  
  employee_list = []
  employee_list.append(employee_1)
  employee_list.append(employee_2)
  employee_list.append(cashier_1)
  
  for employee in employee_list:
      total_wage += employee.raise_pay()
  
      
  total_wage = 0
  for employee in employee_list:
      total_wage += employee.wage
  
  print(total_wage)
  ```

   이런 상황이 문제라는 거야. 

  ```python
  for employee in employee_list:
      total_wage += employee.raise_pay()
  ```

  여기서 에러 터짐.

  ![5_14](./resources/5_22.png)

  `    total_wage += employee.raise_pay()` 여기서 에러가 난거야. 이 부분은 지금 Employee Class의 함수를 쓸꺼라고 가정하고 쓴건데, cashier class는 함수의 파라미터 자체가 다름. 

  ![5_14](./resources/5_23.png)

  이 캐셔 클래스가 문제인거야. 오버라이딩 하면서 자기 멋대로, 파라미터를 추가했음. 

  이런게 바로 **리스코프 치환 원칙 위배**. 

  ```python
  for employee in employee_list:
      total_wage += employee.wage
  ```

  또 다른 에러도 남. 

  ![5_14](./resources/5_24.png)

  이거는 이유가 뭐냐면, cashier의 getter가 그냥 문자열만 리턴함 

  ```python
  @property
  def wage(self):
    return "시급 정보를 알려줄 수 없습니다"
  ```

  이제 말의 의미를 알것 같음. 

  **부모 클래스의 인스턴스(Employee) 사용하는 위치에, 자식 클래스의 인스턴스(Cashier)를 대신 사용했을 때, 코드가 원래 의도대로 작동해야 한다.** 이 말인 즉슨, 자식 클래스의 인스턴스는 부모 클래스의 행동규약을 어기면 안된다는 것. 

  ![5_14](./resources/5_25.png) 

  ![5_14](./resources/5_26.png)

  ![5_14](./resources/5_27.png)

