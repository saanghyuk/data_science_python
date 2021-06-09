#
# 강남역에 엄청난 폭우가 쏟아진다고 가정합시다.
# 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.
# 그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요.
# 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.
#
# 함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고,
# 담기는 빗물의 총량을 리턴해 줍니다.
# 예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다.
# 그러면 0번 인덱스에 높이 3의 건물이, 3번 인덱스에 높이 2의 건물이, 5번 인덱스에 높이 4의 건물이 있다는 뜻입니다.
# 1번, 2번, 4번 인덱스에는 건물이 없습니다.
#
# 그러면 아래의 사진에 따라 총 10 만큼의 빗물이 담길 수 있습니다.
# 따라서 trapping_rain 함수는 10을 리턴하는 거죠.

# 왼쪽에서 제일 높은거, 오른쪽에서 제일 높은 것 중에서
# 나 스스로 보다 큰 만큼거와 양쪽 제일 높은것 중에 작은 것 사이로 찬다.
# def trapping_rain(buildings):
#     # 코드를 작성하세요
#     rain_sum = 0;
#     for i in range(0, len(buildings)):
#         if len(buildings[:i]) == 0 or len(buildings[i+1 : ]) == 0:
#             continue
#         left_max = max(buildings[:i])
#         right_max = max(buildings[i+1:])
#         if buildings[i] < left_max and buildings[i] < right_max:
#             rain_sum += (min(left_max, right_max)  - buildings[i])
#     return rain_sum
# # 테스트
# print(trapping_rain([3, 0, 0, 2, 0, 4]))
# print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# ANSWER
def trapping_rain(buildings):
    total_height = 0  # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n

    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    # left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i - 1])
    # print(left_list)
    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    # right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i + 1])
    # print(right_list)
    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(n):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        # print(i, "번째 건물", max(0, upper_bound - buildings[i]))
        total_height += max(0, upper_bound - buildings[i])

    return total_height

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))