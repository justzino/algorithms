# ๐  ์๋ ฅ ๋ฐ๊ธฐ
## ์์ถ๋ ฅ ์๋ ๋น๊ต
`sys.stdin.readline > raw_input() > input()`

```python
n = int(input())
```
```python
import sys

n = int(sys.stdin.readline())   # ํ ์ค ์๋ ฅ ๋ฐ์ ๋
# n = input()

a = [sys.stdin.readline() for i in range(n)]
```
```python
import sys

for line in sys.stdin:          # ์ฌ๋ฌ์ค ์๋ ฅ ๋ฐ์ ๋
    a, b = map(int, line.split())
    print(a+b)
```
## ์ฃผ์/์ฐธ๊ณ  ์ฌํญ
1. sys.stdin.readline์ ์ฌ์ฉํ  ๋, ๋งจ ๋์ ๊ฐํ๋ฌธ์๊น์ง ๊ฐ์ด ์๋ ฅ๋ฐ๊ธฐ ๋๋ฌธ์ ๋ฌธ์์ด์ ์ ์ฅํ๊ณ  ์ถ์ ๊ฒฝ์ฐ **.strip()**์ ์ถ๊ฐ๋ก ํด ์ฃผ๋ ๊ฒ์ด ์ข๋ค.
21. sys.stdin.readline().split()์ split()์  ๊ณต๋ฐฑ(์คํ์ด์ค, ํญ, ์ํฐ ๋ฑ)์ ๊ธฐ์ค์ผ๋ก ๋ฌธ์์ด์ ๋๋๊ธฐ ๋๋ฌธ์ strip์ ์ถ๊ฐํ  ํ์๊ฐ ์๋ค.(์ฃผ๋ก ์ซ์ ๋ค๋ฃฐ ๋)


## Reference
- https://infinitt.tistory.com/26