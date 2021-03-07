string = input()
count = 0

for i in string:
    print(i, end="")
    count = count + 1

    if count % 10 == 0:
        print("")
