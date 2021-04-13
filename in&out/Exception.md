# 🛠 예외 처리
### 10951 번
## 1. 오류는 어떤 때 발생하는가?
### 1. **FileNotFoundError** : 디렉터리 안에 없는 파일을 열려고 시도했을 때
    ```python
    >>> f = open("나없는파일", 'r')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
    ```
### 2. **ZeroDivisionError** : 0으로 다른 숫자를 나누는 경우
    ```python
    >>> 4 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    ```
### 3. **IndexError** : 리스트 범위에서 벗어난 경우
    ```python
    >>> a = [1,2,3]
    >>> a[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    ```

## 2. 오류 예외 처리 기법
### 1. **try, except문**
    - 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행
    ```python
    try:
       ...
    except:
       ...
    ```
    - except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
    ```python
    try:
       ...
    except 발생 오류:
       ...
    ```
    - 오류 메시지의 내용까지 알고 싶을 때 사용
    ```python
    try:
       ...
    except 발생 오류 as 오류 메시지 변수:
       ...
    ```
    ```python
    try:
       4 / 0
    except ZeroDivisionError as e:
       print(e)
    ```
    > 결과값: division by zero  
### 2. **try .. finally**  
    try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 
    보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.
    ```python
    f = open('foo.txt', 'w')
    try:
        # 무언가를 수행
    finally:
        f.close()
    ```
### 3. **여러개의 오류 처리하기**
    ```python
    try:
        ...
    except 발생 오류1:
       ... 
    except 발생 오류2:
       ...
    ```
    ex1)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except IndexError:
        print("인덱싱 할 수 없습니다.")
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
    > "list index out of range" 오류 메시지가 출력  

    ex3)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except (ZeroDivisionError, IndexError) as e:
        print(e)
    ```
   
## 3. 오류 회피하기
## 4. 오류 일부러 발생시키기
## 5. 예외 만들기

## Reference
- https://wikidocs.net/30#_1