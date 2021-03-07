# 내 풀이
string = input()
result = [-1] * 26

for i in range(len(string)):    # 이렇게 전부 비교하는 것 보다 차라리 find함수 쓰는게 빠르다.
    if result[ord(string[i])-ord('a')] >= 0:
        continue
    else:
        result[ord(string[i])-ord('a')] = i

# print(' '.join(map(str, result)))
print(' '.join([str(i) for i in result]))


# 속도 비교
# string = input()
# for i in range(26):
#     print(string.find(chr(97+i)), end=' ')


# sol(다른사람 풀이)
# string = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in alphabet:
#     print(string.find(i), end = ' ')

