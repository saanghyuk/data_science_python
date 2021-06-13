
class Citizen:
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        self.name = name
        self.__age = age
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        return self.resident_id == id_field

    def can_drink(self):
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        return self.name + "씨는" + str(self.__age) + "살 입니다"

sanghyuk = Citizen("손상혁", '29', '123456')
# print(sanghyuk.__resident_id)
print(sanghyuk.authenticate("123456"))