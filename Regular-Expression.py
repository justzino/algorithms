import re

p = re.compile('[a-z]+')

# 문자열 검색 method: match(), search(), findall(), finditer()
m1 = p.match("python")
m2 = p.match("3 python")
m3 = p.search("python")
m4 = p.search("3 python")
print(m1)
print(m2)
print(m3)
print(m4)
# <re.Match object; span=(0, 6), match='python'>
# None
# <re.Match object; span=(0, 6), match='python'>
# <re.Match object; span=(2, 8), match='python'>


result1 = p.findall("life is too short")
result2 = p.finditer("life is too short")
print(result1)
print(result2)
# ['life', 'is', 'too', 'short']
# <callable_iterator object at 0x0000025A78D0B0C8>
print(*result2, sep='\n')
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>


# match 객체의 method: group(), start(), end(), span()
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
# python
# 0
# 6
# (0, 6)

m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())
# python
# 2
# 8
# (2, 8)

# compile 옵션

# DOTALL, S 옵션
p1 = re.compile('a.b')
p2 = re.compile('a.b', re.DOTALL)
m1 = p1.match('a\nb')
m2 = p2.match('a\nb')
print(m1)
print(m2)
# None
# <re.Match object; span=(0, 3), match='a\nb'>


# IGNORECASE, I 옵션
p = re.compile('[a-z]', re.I)
m1 = p.match('python')
m2 = p.match('Python')
m3 = p.match('PYTHON')
print(m1)
print(m2)
print(m3)
# <re.Match object; span=(0, 1), match='p'>
# <re.Match object; span=(0, 1), match='P'>
# <re.Match object; span=(0, 1), match='P'>


# MULTILINE, M 옵션
p = re.compile("^python\s\w+")
p2 = re.compile("^python\s\w+", re.M)

data = """python one life is too short
python two you need python
python three"""

print(p.findall(data))
print(p2.findall(data))
# ['python one']
# ['python one', 'python two', 'python three']

# VERBOSE, X 옵션 : 문자열에 사용된 whitexpace는 컴파일할 때 제거 (단[] 안에 사용한 whitespace는 제외)
charref1 = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref2 = re.compile(r"""
    &[#]                # Start of a numeric entity reference
    (
     0[0-7]+         # Octal form
    | [0-9]+          # Decimal form
    | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
""", re.VERBOSE)


# 백슬래시 문제
# '\section' 문자열을 찾기 위해서는?
p1 = re.compile('\\section')

# '\\section' 문자열을 찾기 위해서는?
p2 = re.compile('\\\\section')  # 너무 복잡
p3 = re.compile(r'\\section')   # raw string 사용
