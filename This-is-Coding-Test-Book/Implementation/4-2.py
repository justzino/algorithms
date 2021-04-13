n = int(input())

answer_case = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]       # 분, 초 에 나올 수 있는(60 이하의 수 중) 3 이 들어가는 수들
n_case = len(answer_case)       # 60이하의 수 중 3이 들어가는 수의 개수

if n > 3:
    h_case = 1
else:
    h_case = 0

result = h_case * 60 * 60 + (n - h_case + 1) * (n_case * 60 + 60 * n_case - n_case * n_case)

print(result)
