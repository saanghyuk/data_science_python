# 피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
#
# 예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며, 네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이 될 것입니다.
#
# 이러한 방식으로 피보나치 수열의 첫 10개 항은 1, 1, 2, 33, 5, 8, 13, 21, 34, 55입니다.
#
# 파라미터로 1 이상의 자연수 n을 받고, n번째 피보나치 수를 리턴하는 재귀 함수 fib를 쓰세요. 반복문은 쓰면 안됩니다!


# n번째 피보나치 수를 리턴
def fib(n):
    # 코드를 입력하세요.
    if n == 1 or n == 2:
        return 1
    if n >= 3:
        return fib(n-1)+fib(n-2)
# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))