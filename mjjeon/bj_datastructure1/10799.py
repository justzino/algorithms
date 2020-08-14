pipes = input()

cur_pip_cnt = 0
result = 0
for i in range(len(pipes)):
    # () 이 아닐 때
    # 열릴 때 쇠막대기 개수 증가  
    # 닫힐 때 쇠막대기 개수 감소, 닫힌 쇠막대기가 더해지는 갯수 +1  
    if i != len(pipes) - 1 and pipes[i] == '(' and pipes[i+1] != ')':
        cur_pip_cnt += 1
    elif i != 0 and pipes[i] == ')' and pipes[i-1] != '(':
        cur_pip_cnt -= 1
        result += 1
    # () 일 때
    elif i != len(pipes) - 1 and pipes[i] == '(' and pipes[i+1] == ')':
        result += cur_pip_cnt

print(result)