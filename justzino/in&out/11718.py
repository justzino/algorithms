
# 틀림
# import sys
#
# for line in sys.stdin:
#     print(line)

# sol 1
# 기본적으로 입력에 \n이 들어가 있기 때문에 end 파라메터를 통해 줄바꿈을 빈 문자로 바꿔서 줄바꿈 없이 출력
# import sys
#
# for line in sys.stdin:
#     print(line, end='')

# sol 2
while True:
    try:
        print(input())

    except EOFError:
        break
