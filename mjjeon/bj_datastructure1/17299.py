import sys
sys.setrecursionlimit(100001)
cnt = int(sys.stdin.readline().rstrip())
if 1 <= cnt and cnt <= 1000000:
    ngf_list = list(map(int, sys.stdin.readline().rstrip().split()))
    result = [-1 for _ in range(cnt)]
    stack = []

    elem_cnt_list = [0]*1000001

    for i in range(cnt):
        elem_cnt_list[ngf_list[i]] += 1

    for i in range(cnt):
        while len(stack) != 0 and elem_cnt_list[ngf_list[stack[-1]]] < elem_cnt_list[ngf_list[i]]:
            result[stack.pop()] = ngf_list[i]
        stack.append(i)
        
    print(*result)

# ?? 런타임 에러 : 1000000 -> 1000001 배열 크기 때문에
