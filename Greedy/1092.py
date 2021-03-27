import sys


n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

# 각 크레인이 현재 옮겨야 하는 박스의 번호 (0부터 시작)
positions = [0] * n
# 각 박스 옮겼는지 여부
checked = [False] * m

result = 0
count = 0

while True:
    if count == len(boxes):
        break
    for i in range(n):
        while positions[i] < len(boxes):
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날 때까지 반복
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1

print(result)
