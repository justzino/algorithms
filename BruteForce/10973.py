N = int(input())
num = list(map(int, input().split()))


def prev_permutation(seq):
    for i in range(N-2, -1, -1):
        if seq[i] <= seq[i+1]:
            continue
        for j in range(N-1, i, -1):
            if i >= j:
                break
            if seq[i] <= seq[j]:
                continue
            seq[i], seq[j] = seq[j], seq[i]
            a, b = seq[:i+1], seq[i+1:]
            b.sort(reverse=True)
            seq = a + b
            print(*seq)
            return

    print(-1)


prev_permutation(num)
