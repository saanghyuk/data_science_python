# 솔희는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다.
# 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...
# 가능한 최대 수익을 리턴시켜 주는 함수 max_profit을 Tabulation 방식으로 작성해 보세요.
# max_profit은 파라미터 두 개를 받습니다.

# price_list: 개수별 가격이 정리되어 있는 리스트
# count: 판매할 새꼼달꼼 개수
# 예를 들어 price_list가 [0, 100, 400, 800, 900, 1000]이라면,

# 새꼼달꼼 0개에 0원
# 새꼼달꼼 1개에 100원
# 새꼼달꼼 2개에 400원
# 새꼼달꼼 3개에 800원
# 새꼼달꼼 4개에 900원
# 새꼼달꼼 5개에 1000원
# 이렇게 가격이 책정된 건데요. 만약 솔희가 새꼼달꼼 5개를 판매한다면 최대로 얼마를 벌 수 있을까요?
#
# 한 친구에게 3개 팔고 다른 친구에게 2개를 팔면, 800 + 400800+400을 해서 총 1200원의 수익을 낼 수 있겠죠.

def max_profit(price_list, count):
    # 개수별로 가능한 최대 수익을 저장하는 리스트
    # 새꼼달꼼 0개면 0원
    profit_table = [0]

    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
        # 가능한 최대 수익을 profit_table에 넣는다
        if i < 2 :
            profit_table.append(price_list[1])
        else:
            if i < len(price_list):
                profit = price_list[i]
            else:
                profit = 0

            for j in range(1, i // 2 + 1):
                profit = max(profit, profit_table[j] + profit_table[i - j])

            profit_table.append(profit)

    return profit_table[count]

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))


# ANSWER
# def max_profit(price_list, count):
#     # 개수별로 가능한 최대 수익을 저장하는 리스트
#     # 새꼼달꼼 0개면 0원
#     profit_table = [0]
#
#     # 개수 1부터 count까지 계산하기 위해 반복문
#     for i in range(1, count + 1):
#         # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
#         # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
#         if i < len(price_list):
#             profit = price_list[i]
#         else:
#             profit = 0
#
#         # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
#         for j in range(1, i // 2 + 1):
#             profit = max(profit, profit_table[j] + profit_table[i - j])
#
#         profit_table.append(profit)
#
#     return profit_table[count]
