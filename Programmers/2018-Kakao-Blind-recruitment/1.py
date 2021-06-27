def change(n, arr):
    result = []
    for i in arr:
        string = str(bin(i))[2:].zfill(n)
        result.append(list(map(int, string)))
    return result


def sum_arr(n, arr1, arr2):
    array = []
    for i in range(n):
        row = ''
        for j in range(n):
            value = arr1[i][j] or arr2[i][j]
            if value == 1:
                row += '#'
            else:
                row += ' '
        array.append(row)
    return array


def solution(n, arr1, arr2):
    array1 = change(n, arr1)
    array2 = change(n, arr2)
    answer = sum_arr(n, array1, array2)

    return answer
