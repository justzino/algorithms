def selection(data):
    n = len(data)
    for i in range(n-1):
        smallest = i
        for j in range(i + 1, n):
            if data[smallest] > data[j]:
                smallest = j
        data[i], data[smallest] = data[smallest], data[i]


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 3]
selection(array)

print(array)