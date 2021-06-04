
#파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요.
# 반복문을 쓰지 말고, 재귀(recursion)의 개념을 활용해주세요!

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # 코드를 작성하세요.
    str_n = str(n)
    if len(str_n) == 1:
        return int(str_n)
    else:
        number = str_n[0]
        return int(number)+sum_digits(int(str_n[1:]))


# 정답코드
def sum_digits_answer(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits_answer(n // 10)



# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
