X = int(input())
cnt = 0
D = [0] * 1000001 # 런타임에러
D[2] = 1
D[3] = 1
for i in range(4, X+1):
    # (D[i-1] vs D[i/3]) vs D[i/2] 이렇게 비교하기 위해 미리 넣어놓는다.
    # 주석대로 말고, 주석해제된 것 대로..
    # if i%3 == 0:
    #     D[i] = min(D[int(i/3)] + 1, D[i-1] + 1)
    # if i%2 == 0:
    #     D[i] = min(D[int(i/2)] + 1, D[i-1] + 1)
    D[i] = D[i-1] + 1
    if i%3 == 0:
        D[i] = min(D[int(i/3)] + 1, D[i])
    if i%2 == 0:
        D[i] = min(D[int(i/2)] + 1, D[i])
    
print(D[X])

# 틀렸습니다
# 10의 경우 때문에 3으로 나눴을 때 1을 먼저 계산.
# elif로만 구성. 순서에 따라 차이날 수 있는 거라.
# X = int(input())
# cnt = 0
# while X != 1:
#     if X%3 == 1 and X%2 != 0:
#         X -= 1
#         cnt += 1
#     elif X%3 == 0:
#         X //= 3
#         cnt += 1
#     elif X%2 == 0:
#         X //= 2
#         cnt += 1
#     elif X%2 == 1:
#         X -= 1
#         cnt += 1
    
# print(cnt)