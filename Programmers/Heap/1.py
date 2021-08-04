import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        lowest = heapq.heappop(scoville)
        lowest2 = heapq.heappop(scoville)

        new_food = lowest + lowest2 * 2
        heapq.heappush(scoville, new_food)
        answer += 1

    return answer