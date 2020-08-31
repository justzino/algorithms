
def GCD(a, b): 
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)


def LCM(a, b):
    return int(a*b/GCD(a, b))


a, b = map(int, input().split())

print(GCD(a, b), LCM(a, b))