import sys

string = sys.stdin.readline().rstrip()
ans = []

for i in range(len(string)):

    if string[i].isupper():
        if ord(string[i]) + 13 > ord('Z'):
            ans.append(ord(string[i])-13)
        else:
            ans.append(ord(string[i])+13)

    elif string[i].islower():
        if ord(string[i]) + 13 > ord('z'):
            ans.append(ord(string[i])-13)
        else:
            ans.append(ord(string[i])+13)
    else:
        ans.append(ord(string[i]))

for i in range(len(ans)):
    print(chr(ans[i]), end="")

# 그냥 ans[i] = ord(string[i])+13을 해주면 안되고
# ans가 list이므로 append로 해줬어야 했다.
# 빈 list ans에 ans[i]자체가 존재하지 않아서 indexError가 뜬 것 같다.
