N = int(input())
answer = []


# a -> b 로 k번 째 이동
def hanoi(a, b, n):
    count = 0
    if n == 1:
        answer.append((a, b))
        return 1
    count += hanoi(a, 6-a-b, n-1)
    count += hanoi(a, b, 1)
    count += hanoi(6-a-b, b, n-1)
    return count


cnt = hanoi(1, 3, N)
print(cnt)
for a, b in answer:
    print(a, b)