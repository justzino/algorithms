A, B, C = map(int, input().split())
print('{0}\n{1}\n{2}\n{3}'.format((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C)) 