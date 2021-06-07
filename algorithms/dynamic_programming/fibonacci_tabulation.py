# n번째 피보나치 수를 찾아주는 함수 fib_tab을 작성해 보세요.
#
# fib_tab는 꼭 tabulation 방식으로 구현하셔야 합니다!


def fib_tab(n):
    # 코드를 작성하세요.
    fib_list = {}
    if n < 3:
        return 1
    else:
        for i in range(n):
            if i < 2:
                fib_list[str(i+1)] = 1
            else:
                # print(fib_list)
                fib_list[str(i+1)] = fib_list[str(i)]+fib_list[str(i-1)]
    return fib_list[str(n)]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))



# ANSWER
#
# def fib_tab(n):
#     # 이미 계산된 피보나치 수를 담는 리스트
#     fib_table = [0, 1, 1]
#
#     # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
#     for i in range(3, n + 1):
#         fib_table.append(fib_table[i - 1] + fib_table[i - 2])
#
#     # 피보나치 n번째 수를 리턴한다
#     return fib_table[n]
#
# # 테스트
# print(fib_tab(10))
# print(fib_tab(56))
# print(fib_tab(132))