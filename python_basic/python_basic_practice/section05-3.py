
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k, v in q1.items():
    if k =='가을':
        print(v)

q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q2.values():
    if v == '사과' :
        print("Include")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
l4 = [12, 6, 18]
for i in range(len(l4)):
    if i == 0:
        compare = l4[i]
        continue
    else:
        if compare > l4[i]:
            continue
        else:
            compare = l4[i]
print(compare)
