
class Citizen:
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        self.name = name
        self.set_age(age)
        self._resident_id = resident_id

    def authenticate(self, id_field):
        return self._resident_id == id_field

    def can_drink(self):
        return self._age >= Citizen.drinking_age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값으로 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

    def __str__(self):
        return self.name + "씨는" + str(self._age) + "살 입니다"

# sanghyuk = Citizen("손상혁", '29', '123456')
# print(sanghyuk.__resident_id)
# print(sanghyuk.authenticate("123456"))

young = Citizen("younghoon kang", 12, "2345667")
print(young.get_age())
young.set_age(-25)
print(young.get_age())
