class User:
    # initialize 메소드를 여기 쓰세요
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "사용자 : {}, 이메일 : {}, 비밀번호 : ******".format(self.name, self.email)


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

print(user1)
print(user2)
print(user3)
