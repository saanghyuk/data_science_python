
# 이진 탐색 알고리즘을 이미 반복문으로는 구현해 보셨죠? 이번에는 재귀적으로 문제를 해결해 보세요.
# 반드시 재귀(recursion)의 개념을 사용하셔야 합니다. 코드 구현이 꽤 어려우니,
# 천천히 고민해 보시기 바랍니다. 다른 재귀 문제를 풀 때와 마찬가지로 base case와 recursive case를 생각해 내는 것이 핵심입니다!


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    mid = (start_index + end_index) // 2

    if element == some_list[mid]:
        return mid

    if not start_index < end_index:
        return None

    if element >= some_list[mid]:
        # print("first")
        start_index = mid+1
        return binary_search(element, some_list, start_index, end_index)
    elif element <= some_list[mid]:
        # print("second")
        end_index = mid-1
        return binary_search(element, some_list, start_index, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))



#Answer Code

# def binary_search(element, some_list, start_index=0, end_index=None):
#     # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
#     if end_index == None:
#         end_index = len(some_list) - 1
#
#     # start_index가 end_index보다 크면 some_list안에 element는 없다
#     if start_index > end_index:
#         return None
#
#     # 범위의 중간 인덱스를 찾는다
#     mid = (start_index + end_index) // 2
#
#     # 이 인덱스의 값이 찾는 값인지 확인을 해준다
#     if some_list[mid] == element:
#         return mid
#
#     # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
#     if element < some_list[mid]:
#         return binary_search(element, some_list, start_index, mid - 1)
#
#     # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
#     else:
#         return binary_search(element, some_list, mid + 1, end_index)
