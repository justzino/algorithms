import sys
sys.setrecursionlimit(10**6)        # 재귀 쓸때는 깊이 꼭 설저해줄 것!!


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 여러수의 GCD 구하는 함수
def gcd2(nums, n):
    if n < 1:
        return nums[n]
    nums[n - 1] = gcd(nums[n], nums[n - 1])
    return gcd2(nums, n - 1)


N, S = map(int, sys.stdin.readline().split())
locations = list(map(int, sys.stdin.readline().split()))
locations.append(S)
locations.sort()
# gap = list(range(N))
# for i in range(N):
#     gap[i] = locations[i+1] - locations[i]
gap = [locations[i+1] - locations[i] for i in range(N)]

print(gcd2(gap, N-1))
