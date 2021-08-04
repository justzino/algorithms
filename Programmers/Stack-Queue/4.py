from collections import deque


def solution(prices):
    n = len(prices) - 1
    answer = [0 for _ in range(n + 1)]
    stack = []

    for i in range(n):
        tmp = deque()
        while stack:
            top = stack[-1]
            # 가격이 떨어진 경우
            if prices[top] <= prices[i]:
                break
            tmp.appendleft(stack.pop())

        # stack에 있는 시점의 초++
        stack.append(i)
        for index in stack:
            answer[index] += 1
    return answer