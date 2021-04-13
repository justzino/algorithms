
# 동적계획법(Dynamic Programmin, DP)
1. 어떤 문제를 DP로 풀기 위해서는 '최적의 원리' (Principle of Optimality) 가 성립하는지를 확인

2. 메모이제이션(Memoization)을 사용

## 메모이제이션
자꾸만 반복되지만 그 결과 값은 변하지 않는 작은 문제들의 결과값을 저장 하는 것.  

```python
# 백준 9095번
# a(n) = a(n-1) + a(n-2) + a(n-3)
T = int(input())

for _ in range(T):
    n = int(input())
    mem = [0, 1, 2, 4] + [0] * (n - 3)
    for i in range(4, n + 1):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    print(mem[n])
```
## Reference