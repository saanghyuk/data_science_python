# 서로 다른 형태의 정보를 갖고도 User 인스턴스를 만들 수 있죠?
# 하지만 코드가 너무 깁니다. 이럴 때 User 클래스에 클래스 메소드를 두고 사용하면 훨씬 깔끔한 코드로 인스턴스를 생성할 수 있는데요.
# User 클래스의 클래스 메소드 from_string 과 from_list의 내용을 채워봅시다.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 코드를 쓰세요
        return User(*string_params.split(","))

    @classmethod
    def from_list(cls, list_params):
        return User(*list_params)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)