# 거듭 제곱을 계산하는 함수 power를 작성하고 싶습니다. power는
# 파라미터로 자연수 x와 자연수 y를 받고, x^y를 리턴합니다.
# 가장 쉽게 생각할 수 있는 방법은 반복문으로 단순하게 x를 y번 곱해 주는 방법입니다.
#이 알고리즘의 시간 복잡도는 O(y)인데요. O(lgy)로 더 빠르게 할 수는 없을까요?

def power(x, y):
    if y == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    subresult = power(x, y // 2)

    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult



# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))