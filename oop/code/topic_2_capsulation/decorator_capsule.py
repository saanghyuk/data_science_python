
class Citizen:
    drinking_age = 19
    def __init__(self, name, age, resident_id):
        self.name = name
        self._age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        return self.resident_id == id_field

    def can_drink(self):
        return self.age >= Citizen.drinking_age

    @property
    def age(self):
        print("나이를 리턴합니다")
        return self._age

    @age.setter
    def age(self, value):
        print("나이를 설정합니다")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값으로 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

    def __str__(self):
        return self.name + "씨는" + str(self.age) + "살 입니다"

# sanghyuk = Citizen("손상혁", '29', '123456')
# print(sanghyuk.__resident_id)
# print(sanghyuk.authenticate("123456"))

young = Citizen("younghoon kang", 12, "2345667")
print(young.get_age())
young.set_age(30)
print(young.get_age())

