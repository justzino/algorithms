import sys

string = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

cur = 0
leng = len(string)

for i in range(N):

    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == 'L':
        if cur != 0:
            cur -= 1

    elif cmd[0] == 'D':
        if cur != leng:
            cur += 1

    elif cmd[0] == 'B':
        if cur != 0:
            string = string[:cur-1] + string[cur:]
            leng -= 1

    elif cmd[0] == 'P':
        temp = list(cmd[1])
        string = string[0:cur] + temp + string[cur:]
        cur += 1
        leng += 1

print(string)
#
# P를 insert로 바꿔보기
# B를 pop(x)로 해보기.
