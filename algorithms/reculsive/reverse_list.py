# 파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해 주는 재귀 함수 flip을 쓰세요.
# 반복문은 쓰면 안됩니다!
# 파라미터 some_list를 거꾸로 뒤집는 함수

def flip(some_list):
    # 코드를 입력하세요.
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    else:
        return some_list[-1:] + flip(some_list[:-1])


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(some_list[-1:])
# print(some_list[:-1])
# print(some_list)
some_list = flip(some_list)
print(some_list)


















