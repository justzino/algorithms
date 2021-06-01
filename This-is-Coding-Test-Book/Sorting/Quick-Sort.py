def qsort(data):
    if len(data) <= 1:
        return data

    left, right = [], []
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return qsort(left) + [pivot] + qsort(right)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
qsort(array)
print(array)
