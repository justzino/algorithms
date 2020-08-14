
n, m = map(int, input().split())

result = []
temp_queue = list(range(1, n+1))

i = 0
while len(temp_queue) > 0:
    i = (i + m - 1)%len(temp_queue)
    result.append(temp_queue.pop(i))

print(''.join(str(result)).replace('[', '<').replace(']', '>'))



# 설명: https://kgh940525.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-1158-%EC%A1%B0%EC%84%B8%ED%8D%BC%EC%8A%A4-%EB%AC%B8%EC%A0%9C