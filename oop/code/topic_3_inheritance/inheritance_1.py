class Employee:
    """직원클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + "직원: " + self.name


class Cashier(Employee):
    raise_percentage = 1.05
    burger_price = 4000
    def __init__(self, name, wage, number_sold):
        """인스턴스 변수 설정"""
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해 주세요")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name


class DeliveryMan(Employee):
    pass

sanghyuk = DeliveryMan("손상혁", 9000)
sanghyuk.raise_pay()
print(sanghyuk.wage)
print(sanghyuk)

sanghyuk2 = Cashier("손상혁", 9000, 4)
print(sanghyuk2)


print(Cashier.mro())
