import heapq
import sys
input = sys.stdin.readline

left_max_pq = []
right_min_pq = []

N = int(input())

for _ in range(N):
    x = int(input())

    # 길이가 같으면 왼쪽에 저장 -> 중앙값 = left_max_pq 의 top
    if len(left_max_pq) == len(right_min_pq):
        heapq.heappush(left_max_pq, (-x, x))
    else:
        heapq.heappush(right_min_pq, (x, x))

    if right_min_pq and left_max_pq[0][1] > right_min_pq[0][1]:
        left = heapq.heappop(left_max_pq)[1]    # 이부분 [1] 해줘야하는거 주의!!
        right = heapq.heappop(right_min_pq)[1]
        heapq.heappush(left_max_pq, (-right, right))
        heapq.heappush(right_min_pq, (left, left))

    print(left_max_pq[0][1])