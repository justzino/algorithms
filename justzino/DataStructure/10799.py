# 원리 : 가장 윗 레벨(마지막)의 쇠막대들 에는 (갯수+1) 해서 곱하기
# 즉, 같은 레벨의 쇠막대를 자르는게 아니고, 닫혔다가 새로 열리면 그놈도 가장 윗 레벨

string = input()
count = [0 for _ in range(100005)]   # count of each level
count_on = False    # '(' 다음에 바로 닫히는 ')'만 count
new_stick = False   # '('가 연속 2개 와서 new_stick == 0 상태에서 ')' 가 2개 이상 오면 새 stick 이닫힐 때, count+1
level = 0

max_level = 0
result = 0

stack = []
stack_append = stack.append     # list comprehension
stack_pop = stack.pop

for c in string:
    if c == '(':
        level += 1
        stack_append(c)
        if count_on:
            new_stick = True        # '('가 연속해서 오는 경우
        count_on = True

    elif c == ')':
        level -= 1
        if level > max_level:
            max_level = level
        if count_on:
            count[level] += 1
        elif not count_on:      # ')'가 연속해서 오는 경우
            count[level] += 1

        stack_pop()
        count_on = False

for i in range(1, max_level + 1):
    result += count[i] * i

print(result)