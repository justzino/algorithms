n = int(input())

array = []
for _ in range(n):
    a, b = input().split()
    array.append((a, int(b)))

# key 를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
