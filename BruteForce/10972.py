N = int(input())
s = list(map(int, input().split()))


def next_permutation(seq):
    n = len(seq)-1
    for i in range(n, 0, -1):
        if seq[i-1] >= seq[i]:
            continue

        for j in range(n, i-1, -1):
            if i-1 >= j:
                break
            if seq[i-1] >= seq[j]:
                continue
            seq[i-1], seq[j] = seq[j], seq[i-1]
            a, b = seq[:i], seq[i:]
            b.sort()
            seq = a + b
            print(*seq)
            return

    print(-1)


next_permutation(s)
