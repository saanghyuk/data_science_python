#
# 이미 sublist_max 함수를 각각 Brute Force과 Divide and Conquer 방식으로 작성했는데요.
# Brute Force로 풀었을 때는 시간 복잡도가 O(n^2),
# Divide and Conquer를 사용했을 때는 O(nlgn)였습니다.
#
# 이번 과제에서는 시간 복잡도를 O(n)O(n)로 한 번 더 단축해보세요!


# 현재 인덱스를 포함한 값중에 제일 큰 profit과
# 현재 인덱스를 포함하지 않은 값중에 제일 큰 값을 max()한 것
# 즉, 전체를 두 케이스로 나누는 것. 현재 index를 반드시 포함한 최댓값, 포함하지 않은 값들 중 최댓값.
# 둘 중에 더 최댓값을 사용하는 것.

def sublist_max(profits):
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        # 이전 max_check에는 그 바로 전 숫자를 반드시 포함하는 값들 중에 최대값이 들어 있음.
        max_check = max(max_check + profits[i], profits[i])

        # 최대 구간 합을 비교를 통해 정한다
        # 이전 max_profit_so_far에는 지금 숫자가 배재된 상태로의 최댓값이 들어있음.
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far



# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
