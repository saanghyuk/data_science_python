
def merge(list1, list2):
    # 코드를 작성하세요.
    merged_list = []
    # print(len([])==0)
    while len(list1) != 0 or len(list2) != 0:
        if len(list1) == 0 :
            merged_list+=list2
            return merged_list
        if len(list2) == 0 :
            merged_list += list1
            return merged_list
        if list1[0] >= list2[0]:
            merged_list.append(list2.pop(0))
        else:
            merged_list.append(list1.pop(0))

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) < 2:
        return my_list
    mid = (len(my_list) // 2)
    left_half = my_list[: mid]
    right_half = my_list[mid : ]

    return merge(merge_sort(left_half), merge_sort(right_half))


# 테스트
# print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
# print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
