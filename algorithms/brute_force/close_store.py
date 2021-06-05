# 스다벅스는 줄어든 매출 때문에 지점 하나를 닫아야 하는 위기에 처해 있습니다.
# 어떤 지점을 닫는 게 회사에 타격이 적을지 고민이 되는데요. 서로 가까이 붙어 있는 매장이 있으면, 그 중 하나는 없어져도 괜찮지 않을까 싶습니다.
# 사장님은 비서 태호에게, 직선 거리가 가장 가까운 두 매장을 찾아서 보고하라는 임무를 주셨습니다.


# 제곱근 사용을 위한 sqrt 함수
from math import sqrt
from itertools import combinations



# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    combination_list = [i for i in combinations(coordinates, 2)]
    distance_list = [distance(*i) for i in combinations(coordinates, 2)]
    min_distance = min(distance_list)
    return list(combination_list[distance_list.index(min_distance)])







# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))



# ANSWER
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair