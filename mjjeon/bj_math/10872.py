n = int(input())
result = 1
if n > 1:
    for i in range(2, n+1): 
        result = result * i
result = str(result)
cnt = 0
for i in result[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)