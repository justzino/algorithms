def calc(priority, n, expression):
    # priority 연산자 우선순위 모음 / n 우선순위 --> 낮은 것부터 0, 1, 2 / expression 더 낮은 우선순위에서 쪼개진 식 문자열
    if n == 2:  # 가장 높은 우선순위에 도달했을 때, 계산한다.
        return str(eval(expression))
    if priority[n] == '*':  # 먼저 쪼갠 애들부터 계산한다.
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))

    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer
