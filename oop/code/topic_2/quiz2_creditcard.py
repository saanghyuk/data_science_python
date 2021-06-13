class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        # 코드를 쓰세요
        self._name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if 0 <= new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")


card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)