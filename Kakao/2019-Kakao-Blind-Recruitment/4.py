import heapq


def solution(food_times, k):
    length = len(food_times)
    count = 0

    if sum(food_times) <= k:
        return -1

    for i in range(length):
        food_times[i] = (food_times[i], i + 1)

    heapq.heapify(food_times)  # min heapq (남은양, 음식번호) 순서

    while food_times:
        ### 테스트용
        # print(food_times, f"k={k}")

        now_amount, now_food = heapq.heappop(food_times)
        now_amount = now_amount - count

        # now * l 음식 양 <= k 인 경우
        if now_amount * length < k:
            count += now_amount
            k -= now_amount * length
            length -= 1
            continue

        if k == 0:
            return now_food

        # now * l 음식 양 > k 인 경우 -> k번 돌려서 찾기
        heapq.heappush(food_times, (now_amount, now_food))
        food_times.sort(key=lambda x: x[1])
        q, r = divmod(k, length)

        return food_times[r][1]

    return -1