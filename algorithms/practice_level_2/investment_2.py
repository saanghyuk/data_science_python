#
# 저번 챕터에서 sublist_max 함수를 Brute Force 방식으로 작성했습니다.
# 이번에는 같은 문제를 Divide and Conquer 방식으로 풀어볼 텐데요.
# 시간 복잡도는 O(nlgn)이 되어야 합니다.
#
# 이번 sublist_max 함수는 3개의 파라미터를 받습니다.
#
# profits: 며칠 동안의 수익이 담겨 있는 리스트
# start: 살펴볼 구간의 시작 인덱스
# end: 살펴볼 구간의 끝 인덱스
# sublist_max는 profits의 start부터 end까지 구간에서 가능한 가장 큰 수익을 리턴합니다.
#
# 합병 정렬을 구현할 때 merge_sort 함수를 깔끔하게 작성하기 위해
# 추가로 merge 함수를 작성했던 것 기억 나시나요?
# 마찬가지로 퀵 정렬을 구현할 때 quicksort 함수에 추가로 partition 함수를 작성했습니다.
# 이번에도 sublist_max 함수에 추가로 새로운 함수를 작성하면 도움이 되실 겁니다.

def max_crossing_sum(profits, start, end):
    mid = (start + end) // 2      # 중간 인덱스
    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0                  # 왼쪽 누적 수익
    left_max = profits[mid]       # 왼쪽 최고 수익; 왼쪽 반 중 가장 오른쪽 값으로 초기화

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0                 # 오른쪽 누적 수익
    right_max = profits[mid + 1]  # 오른쪽 최고 수익; 오른쪽 반 중 가장 왼쪽 값으로 초기화

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    # 범위에 하나의 항목밖에 없으면, 그 항목을 리턴한다
    if start == end:
        return profits[start]

    # 중간 인덱스
    mid = (start + end) // 2

    # 상황별로 최대 수익을 구한다
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))