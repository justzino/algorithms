a = int(input())
b = a

for i in range(1, a):
    if i == 1:
        print(" "*(b-i) + "*")
    else:
        print(" "*(b-i) + "*" + " "*(2*i-3) + "*")
print("*"*(2*a-1))
