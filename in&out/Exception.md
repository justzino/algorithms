# ๐  ์์ธ ์ฒ๋ฆฌ
### 10951 ๋ฒ
## 1. ์ค๋ฅ๋ ์ด๋ค ๋ ๋ฐ์ํ๋๊ฐ?
### 1. **FileNotFoundError** : ๋๋ ํฐ๋ฆฌ ์์ ์๋ ํ์ผ์ ์ด๋ ค๊ณ  ์๋ํ์ ๋
    ```python
    >>> f = open("๋์๋ํ์ผ", 'r')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: '๋์๋ํ์ผ'
    ```
### 2. **ZeroDivisionError** : 0์ผ๋ก ๋ค๋ฅธ ์ซ์๋ฅผ ๋๋๋ ๊ฒฝ์ฐ
    ```python
    >>> 4 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    ```
### 3. **IndexError** : ๋ฆฌ์คํธ ๋ฒ์์์ ๋ฒ์ด๋ ๊ฒฝ์ฐ
    ```python
    >>> a = [1,2,3]
    >>> a[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    ```

## 2. ์ค๋ฅ ์์ธ ์ฒ๋ฆฌ ๊ธฐ๋ฒ
### 1. **try, except๋ฌธ**
    - ์ค๋ฅ ์ข๋ฅ์ ์๊ด์์ด ์ค๋ฅ๊ฐ ๋ฐ์ํ๋ฉด except ๋ธ๋ก์ ์ํ
    ```python
    try:
       ...
    except:
       ...
    ```
    - except๋ฌธ์ ๋ฏธ๋ฆฌ ์ ํด ๋์ ์ค๋ฅ ์ด๋ฆ๊ณผ ์ผ์นํ  ๋๋ง except ๋ธ๋ก์ ์ํ
    ```python
    try:
       ...
    except ๋ฐ์ ์ค๋ฅ:
       ...
    ```
    - ์ค๋ฅ ๋ฉ์์ง์ ๋ด์ฉ๊น์ง ์๊ณ  ์ถ์ ๋ ์ฌ์ฉ
    ```python
    try:
       ...
    except ๋ฐ์ ์ค๋ฅ as ์ค๋ฅ ๋ฉ์์ง ๋ณ์:
       ...
    ```
    ```python
    try:
       4 / 0
    except ZeroDivisionError as e:
       print(e)
    ```
    > ๊ฒฐ๊ณผ๊ฐ: division by zero  
### 2. **try .. finally**  
    try๋ฌธ์๋ finally์ ์ ์ฌ์ฉํ  ์ ์๋ค. finally์ ์ try๋ฌธ ์ํ ๋์ค ์์ธ ๋ฐ์ ์ฌ๋ถ์ ์๊ด์์ด ํญ์ ์ํ๋๋ค. 
    ๋ณดํต finally์ ์ ์ฌ์ฉํ ๋ฆฌ์์ค๋ฅผ closeํด์ผ ํ  ๋์ ๋ง์ด ์ฌ์ฉํ๋ค.
    ```python
    f = open('foo.txt', 'w')
    try:
        # ๋ฌด์ธ๊ฐ๋ฅผ ์ํ
    finally:
        f.close()
    ```
### 3. **์ฌ๋ฌ๊ฐ์ ์ค๋ฅ ์ฒ๋ฆฌํ๊ธฐ**
    ```python
    try:
        ...
    except ๋ฐ์ ์ค๋ฅ1:
       ... 
    except ๋ฐ์ ์ค๋ฅ2:
       ...
    ```
    ex1)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except ZeroDivisionError:
        print("0์ผ๋ก ๋๋ ์ ์์ต๋๋ค.")
    except IndexError:
        print("์ธ๋ฑ์ฑ ํ  ์ ์์ต๋๋ค.")
    ```
    ex2)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
    ```
    > "list index out of range" ์ค๋ฅ ๋ฉ์์ง๊ฐ ์ถ๋ ฅ  

    ex3)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except (ZeroDivisionError, IndexError) as e:
        print(e)
    ```
   
## 3. ์ค๋ฅ ํํผํ๊ธฐ
## 4. ์ค๋ฅ ์ผ๋ถ๋ฌ ๋ฐ์์ํค๊ธฐ
## 5. ์์ธ ๋ง๋ค๊ธฐ

## Reference
- https://wikidocs.net/30#_1