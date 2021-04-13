# 완전 탐색(Brute Forcing)
# 탐색 해야할 데이터의 개수가 100만개 이하일 때 사용.

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있따면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
