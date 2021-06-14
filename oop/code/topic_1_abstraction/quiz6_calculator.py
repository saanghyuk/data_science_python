# 다음 조건들을 보고 계산기 클래스인 SimpleCalculator 클래스의 정적 메소드들을 완성해보세요.
#
# 정적 메소드
# add: 파라미터로 받은 두 숫자의 합을 리턴한다
# subtract: 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
# multiply: 파라미터로 받은 두 숫자의 곱을 리턴한다
# divide: 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다

class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        # 파라미터로 받는 두 숫자의 합을 리턴한다
        return first_number+second_number


    @staticmethod
    def subtract(first_number, second_number):
        # 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
        return first_number - second_number


    @staticmethod
    def multiply(first_number, second_number):
        # 파라미터로 받는 두 숫자의 곱을 리턴한다
        return first_number * second_number



    @staticmethod
    def divide(first_number, second_number):
        # 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다
        return first_number / second_number




# 계산기 인스턴스 생성
calculator = SimpleCalculator()

# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))


