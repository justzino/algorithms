def bubble(arr):
    length = len(arr)
    counter = 0
    last = length - 1
    for i in range(length-1):
        flag = 0

        for j in range(last):
            print(arr)
            counter += 1
            if arr[j] > arr[j + 1]:
                last = j + 1
                flag += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if flag == 0:
            break
    return counter


if __name__ == "__main__":
    li = [(1, 0), (4, 1), (3, 2), (8, 3), (5, 4)]
    print(bubble(li))
    print(li)

