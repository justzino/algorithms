def permutations(arr, level):
    result = []
    if level == 0:
        return [[]]

    for i, num in enumerate(arr):
        for p in permutations(arr[:i] + arr[i+1:], level-1):
            result += [[num] + p]

    return result


# main
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