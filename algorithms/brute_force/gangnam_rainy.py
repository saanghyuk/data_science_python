# 강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.
# 그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.
# 함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.
# 예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다.
# 그러면 0번 인덱스에 높이 33의 건물이, 3번 인덱스에 높이 2의 건물이, 5번 인덱스에 높이 4의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.
# 그러면 아래의 사진에 따라 총 10 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠.

def trapping_rain(buildings):
    # 코드를 작성하세요
    sum_rain=0;
    for i in range(1, len(buildings)-1):
        # print(i)
        # print(i, "번째 건물")
        # print(min(max(buildings[:i]), max(buildings[i+1:])))
        if min(max(buildings[:i]), max(buildings[i + 1:])) <= buildings[i]:
            continue
        sum_rain += min(max(buildings[:i]), max(buildings[i + 1:])) - buildings[i]
    return sum_rain
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))




# ANSWER
# def trapping_rain(buildings):
#     # 총 담기는 빗물의 양을 변수에 저장
#     total_height = 0
#
#     # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
#     # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
#     for i in range(1, len(buildings) - 1):
#         # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
#         max_left = max(buildings[:i])
#         max_right = max(buildings[i:])
#
#         # 현재 인덱스에 빗물이 담길 수 있는 높이
#         upper_bound = min(max_left, max_right)
#
#         # 현재 인덱스에 담기는 빗물의 양을 계산
#         # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
#         total_height += max(0, upper_bound - buildings[i])
#
#     return total_height