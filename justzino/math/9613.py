import sys


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 문제 잘못 이해해서 여러수의 GCD구하는 함수 만듬. - 사용x
def gcd2(nums_list, n):
    if n <= 1:
        return nums_list[n]
    nums_list[n-1] = gcd(nums_list[n], nums_list[n-1])
    return gcd2(nums_list, n-1)


def gcd3(nums_list, n, s):
    if n <= 1:
        return s
    for i in range(1, n):
        s += gcd(nums_list[n], nums_list[i])
    return gcd3(nums_list, n-1, s)


t = int(sys.stdin.readline())
for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))     # nums[0] = n
    sum = 0
    print(gcd3(nums, nums[0], sum))
