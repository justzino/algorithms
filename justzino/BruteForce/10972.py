from itertools import permutations

N = int(input())
point_num = list(map(int, input().split()))


def func(cnt):
    seqs = list(permutations([i for i in range(1, N + 1)], N))
    flag = 0

    for seq in seqs:
        if flag == 1:
            print(*seq)
            return

        if cnt == N:
            print('-1')
            return

        if point_num != list(seq):
            cnt += 1
            continue
        flag = 1


func(0)
