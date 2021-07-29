# String 정리

### 진법 및 아스키코드 변환

|     method     |             Return type : 설명              |                    Ex                    |
| :------------: | :-----------------------------------------: | :--------------------------------------: |
|     chr()      |   string : 숫자(아스키 코드) → 문자 변환    |       chr(65) = 'A', chr(97) = 'a'       |
|     ord()      |       int : 문자 → 숫자(아스키 코드)        |       ord('A') = 65, ord('a') = 97       |
| int(num, base) | int : n진법으로 표기된 문자열 → 10진법 숫자 |           int('3212', 5) = 432           |
|     bin()      |        string : 2진수 문자열로 변환         | bin(10) = '0b1010', bin(0o12) = '0b1010' |
|     oct()      |        string : 8진수 문자열로 변환         |   oct(10) = '0o12', oct(0xa) = '0o12'    |
|     hex()      |        string : 16진수 문자열로 변환        |    hex(10) = '0xa', hex(0o12) = '0xa'    |

#### 10진수 -> n 진수
```python
NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    
    if not q:
        return n
    
    return numeral_system(q, base) + n 
```


### string Method

|                     Method                     |                        Return type : 설명 (대 소문자 구분)                        |                                                                              Ex                                                                               |
| :--------------------------------------------: | :-------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                    len(str)                    |                                int : 문자열의 길이                                |                                                            str = 'Hello World' <br> len(str) -> 11                                                            |
|                  str.split()                   |                     list : 문자열을 기준에 따라 나누어 return                     |                                                  str = 'Hello World' <br> str.split() -> ['Hello', 'World']                                                   |
|                  str.strip()                   |           string : 문자열의 양쪽 끝에 해당 문자가 있으면 지운 후 return           |                                                          str = '.abc.' <br> str.strip('.') -> 'abc'                                                           |
|                   str.join()                   |            string : string을 list파라미터의 중간에 넣어 합친후 return             |                          a = ['Hello', 'World'] <br> ' '.join(a) -> 'Hello World' <br> str = 'abc' <br> str.join('123') -> 1abc2abc3                          |
|                 str.replace()                  | string : 문자열의 특정 부분을 바꾸어 return <br> 특정 부분이 없다면 그대로 return |                                           str = 'Hello World' <br> str.replace('World', 'Python') -> 'Hello Python'                                           |
|        str.find(문자열, 찾기시작할위치)        |         int/-1 : 매개변수로 입력한 문자열의 index return 없으면 return -1         |                               str = 'aa bb aa bb' <br> str.find('bb') -> 3 <br> str.find('bb', 4) -> 9 <br> str.find('h') -> -1                               |
|                  str.index()                   |             int/ValueError : find와 동일하나 없으면 return ValueError             |                                     str = 'abc가나다123' <br> str.index('가나다') -> 4 <br> str.index('d') -> ValueError                                      |
|        str.startswith(문자열, 시작지점)        |           bool : 매개변수로 문자열이 시작하면 True, 그렇지 않으면 False           |                   str = 'aabbaa' <br> str.startswith('aa') -> True <br> str.startswith('AA') -> False <br> str.startswith('aa', 4) -> True                    |
| str.endswith(문자열, 문자열의시작, 문자열의끝) |            bool : 매개변수로 문자열이 끝나면 True, 그렇지 않으면 False            |                                      str = 'World' <br> str.endswith('l') -> False <br> str.endswith('l', 0, 4) -> True                                       |
|                  str.count()                   |                        int : 매개변수의 문자열 개수 return                        |                                   str = 'Hello' <br> str.count('l') -> 2 <br> str.count('ll') -> 1 <br> str.count('x') -> 0                                   |
|                 str.isalpha()                  |           bool : 문자열이 영어, 한글로만 이루어졌으면 True 아니면 False           |                               str = 'abc가나다' <br> str.isalpha() -> True <br> str = 'abc 가나다' <br> str.isalpha() -> False                                |
|                 str.isdigit()                  |              bool : 문자열이 숫자로만 이루어졌으면 True 아니면 False              |                                      str = '123' <br> str.isdigit() -> True <br> str = '1 23'<br> str.isdigit() -> False                                      |
|                 str.isalnum()                  |        bool : 문자열이 영어, 한글, 숫자로만 이루어졌으면 True 아니면 False        |                              str = 'abc가나다123' <br> str.isalnum() -> True <br> str = 'ab 가나 12' <br> str.isalnum() -> False                              |
|                 str.islower()                  |      bool : 문자열 중 알파벳이 모두 소문자로만 되어졌으면 True 아니면 False       | str = 'abc 123 가나다' <br> str.islower() -> True <br> str = 'Abc 123 가나다' <br> str.islower() -> False <br> str = '123 가나다' <br> str.islower() -> False |
|                 str.isupper()                  |      bool : 문자열 중 알파벳이 모두 대문자로만 되어졌으면 True 아니면 False       | str = 'ABC 123 가나다' <br> str.isupper() -> True <br> str = 'aBC 123 가나다' <br> str.isupper() -> False <br> str = '123 가나다' <br> str.isupper() -> False |
|                  str.lower()                   |                       string : 문자열을 모두 소문자로 변환                        |                                                  str = 'Abc 123 가나다' <br> str.lower() -> 'abc 123 가나다'                                                  |
|                  str.upper()                   |                       string : 문자열을 모두 대문자로 변환                        |                                                  str = 'Abc 123 가나다' <br> str.upper() -> 'ABC 123 가나다'                                                  |
|                   str[::-1]                    |                             string : 문자열을 뒤집기                              |                                                              str = 'abc' <br> str[::-1] -> 'cba'                                                              |
|                str.capitalize()                |                string : 문자열의 첫 글자를 대문자로 바꾸어 return                 |                                                  str = 'hello world' <br> str.capitalize() -> 'Hello world'                                                   |
|                  str.title()                   |           string : 문자열에서 알파벳의 첫 글자를 대문자로 바꾸어 return           |                                                 str = 'hello wo세상rld' <br> str.title() -> 'Hello Wo세상Rld'                                                 |
|          str.rjust(문자열 길이, 문자)          |          string : 오른쪽 정렬, 문자열 왼쪽에 입력한 문자로 채워서 return          |                                                         str = 'abc' <br> str.rjust(5, '#') -> '##abc'                                                         |
|          str.ljust(문자열 길이, 문자)          |          string : 왼쪽 정렬, 문자열 오른쪽에 입력한 문자로 채워서 return          |                                                         str = 'abc' <br> str.ljust(5, '#') -> 'abc##'                                                         |
|             str.zfill(문자열 길이)             |                        string : 0으로 왼쪽을 채워서 return                        |                                                           str = 'abc' <br> str.zfill(5) -> '00abc'                                                            |
