n = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 coin으로 거슬러 줄 수 있는 개수 세기
    n %= coin

print(count)
