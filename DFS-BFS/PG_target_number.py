def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    dfs(0, 0)
    return answer


def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers and target != 0:
        return 0
    else:
        return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])
