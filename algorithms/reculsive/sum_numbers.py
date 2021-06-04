# n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다.
# 파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요.
# n은 1 이상의 자연수라고 가정합시다.
# 함수 안에 반복문은 쓰면 안됩니다!

def triangle_number(n):
    if n == 1:
        return 1
    # 코드를 입력하세요
    if n > 1:
        return n + triangle_number(n - 1)


# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))