# 구간 합(prefix sum) 문제

n, target = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 투포인터 설정
small = 100000
start = 0
end = 1

while end <= n:
    if prefix_sum[end] - prefix_sum[start] >= target:
        small = min(small, end - start)
        start += 1
        
    # 부분 합이 target 보다 작은 경우
    else:
        end += 1

# 답이 없는 경우
if small != 100000:
    print(small)
else:       # 답이 있는 경우
    print(0)
