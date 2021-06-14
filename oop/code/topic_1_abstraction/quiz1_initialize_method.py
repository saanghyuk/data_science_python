# 인스턴스 변수는 항상 사용하기 전에 미리 설정해야 합니다.
# User 클래스의 인스턴스를 4개 만들고 각 인스턴스에 인스턴스 변수를 설정해봅시다.

class User:
    # initialize 메소드를 여기 쓰세요
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
