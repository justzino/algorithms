N = int(input())
member = []

for i in range(N):
    age, name = input().split()
    member.append((age, i, name))

member.sort()
for i in range(N):
    age = member[i][0]
    name = member[i][2]
    answer = age + ' ' + name
    print(answer)
