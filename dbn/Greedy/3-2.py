# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
nums = list(map(int, input().split()))

nums.sort()         # 입력받은 수 정렬
first = nums[-1]        # 가장 큰 수
second = nums[-2]       # 두 번째로 큰수

sum_seq = first * k + second        # 반복하는 패턴 합
num_seq, lasts = divmod(m, k+1)     # 패턴이 나올 수 있는 총 개수, 남은 개수

result = sum_seq * num_seq + first * lasts      # 패턴 합 * 패턴 개수 + 가장큰수 * 남은 개수
print(result)
