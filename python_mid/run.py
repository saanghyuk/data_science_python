

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def horizontal_flip(list):
    ### 코드를 작성해 주세요 ###

    for i in range(len(list)):
        list[i] = list[i][::-1]
    return list

print(horizontal_flip(list))