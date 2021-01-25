from itertools import permutations


N = int(input())
seqs = list(permutations(range(1, N+1), N))

for seq in seqs:
    print(*seq)
