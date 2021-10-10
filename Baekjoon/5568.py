from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    cards.append(input())

cases = permutations(cards, k)
numbers = set()

for case in cases:
    numbers.add(int(''.join(list(case))))

print(len(numbers))