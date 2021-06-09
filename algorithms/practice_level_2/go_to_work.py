# 영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.
# 어느 날 문득, 호기심이 생겼습니다. 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?
# 계단 4개를 올라간다고 가정하면, 이런 방법들이 있습니다.
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
from itertools import combinations_with_replacement
#
# for i in combinations_with_replacement([1,2,3,4],2) :
#     print(i,end=" ")


def staircase(n):
    # 코드를 작성하세요.
    if n == 0 or n == 1:
        return n
    number_of_combination = 0
    for i in range((n//2)+1):
        # print(i)
        # print(combinations_with_replacement([ k for k in range(n - 2*i)], i))
        for k in combinations_with_replacement([ k for k in range(n - (2*i)+1)], i):
            number_of_combination += 1
    return number_of_combination
# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))


#ANSWER
# n번 계단으로 가기 위해서는 n - 1번 계단 또는 n - 2번 계단에서 올라가야 합니다.
# 수학적으로 staircase(n)은 staircase(n - 1) + staircase(n - 2)로 표현이 가능합니다. 어디서 많이 보던 연산 아닌가요?

def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
