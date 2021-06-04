# 카드 두 뭉치가 있습니다.
# 왼쪽 뭉치에서 카드를 하나 뽑고 오른쪽 뭉치에서 카드를 하나 뽑아서, 두 수의 곱이 가장 크게 만들고 싶은데요. 어떻게 하면 가장 큰 곱을 구할 수 있을까요?
# 함수 max_product는 리스트 left_cards와 리스트 right_cards를 파라미터로 받습니다.
# left_cards는 왼쪽 카드 뭉치의 숫자들, right_cards는 오른쪽 카드 뭉치 숫자들이 담겨 있고,
# max_product는 left_cards에서 카드 하나와 right_cards에서 카드 하나를 뽑아서 곱했을 때 그 값이 최대가 되는 값을 리턴합니다.

def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    max = 0;
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            mul = left_cards[i] * right_cards[j]
            # print(mul)
            if max < mul:
                max = mul
            else:
                continue
    return max
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))


# ANSWER
# def max_product(left_cards, right_cards):
#     # 현재까지 최댓값을 담기 위한 변수
#     # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
#     max_product = left_cards[0] * right_cards[0]
#
#     # 가능한 모든 조합을 보기 위한 중첩 반복문
#     for left in left_cards:
#         for right in right_cards:
#             # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
#             max_product = max(max_product, left * right)
#
#     # 찾은 최댓값을 리턴한다
#     return max_product