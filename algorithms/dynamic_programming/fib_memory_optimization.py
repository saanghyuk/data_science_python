
# 영상에서 보셨듯, nn번째 피보나치 수를 계산하기 위해서는 가장 최근에 계산한 두 값만 알면 됩니다.
#
# 공간 복잡도 O(1)O(1)로 fib_optimized 함수를 작성하세요.
#


def fib_optimized(n):
    # 코드를 작성하세요.
    previous = 1
    current = 1
    for i in range(3, n+1):
        previous, current = current, current+previous
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))


# ANSWER
# def fib_optimized(n):
#     current = 1
#     previous = 0
#
#     # 반복적으로 위 변수들을 업데이트한다.
#     for i in range(1, n):
#         current, previous = current + previous, current
#
#     # n번재 피보나치 수를 리턴한다.
#     return current