class User:
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요 저는 {} 입니다.".format(self.name))

    def check_name(self, name):
        # 파라미터로 받는 Name이 유저의 이름과 같은지 불린으로 리턴해 주는 메소드
        return self.name == name

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다. ")
        else:
            print("로그인 실패, 없는 아이디 이거나 잘못된 비밀번호입니다.")

user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
print(user1.__dir__())
user1.email = "captain@gmail.com"
user1.password = "12345"

user2.name = "손상혁"
user2.email = "captain2@gmail.com"
user2.password = "6493"

user3.name = "이미영"
user3.email = "myoung@gmail.com"
user3.password = "115215"

print(user1.email)
print(user2.password)
print(user3.name)

#Instance Method
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)
# user1.say_hello(user1)


# user1.login(user1, "captain@gmail.com", "12345")
user1.login("captain@gmail.com", "12345")

print(user1.check_name("김대위"))
print(user1.check_name("손상혁"))

