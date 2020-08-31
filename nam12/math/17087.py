# import sys
# from sys import stdin


# input = stdin.readline().rstrip().split()

# N, S = map(int, input)

# arr = list(map(int, input))

# arr2 = list(map(int, (stdin.readline().rstrip().split())))

# print(N, S, arr, arr2)

# 이렇게 입력하면 왜 3 3 [3, 3] [1, 7, 17]로 입력이 되지??


# N, S = map(int, sys.stdin.readline().rstrip().split())

# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# arr.sort()

# first = arr[0]
# last = arr[N-1]

# max_distance = 1
# d = 1

# while (d <= min(abs(first - S), abs(last - S))):
#     cnt = 0

#     for i in range(S, first-1, -d):  # 왼쪽으로
#         if i in arr:
#             cnt += 1
#     for i in range(S, last+1, d):  # 오른쪽으로
#         if i in arr:
#             cnt += 1

#     if cnt == N:
#         max_distance = d
#     d += 1
# print(max_distance)
