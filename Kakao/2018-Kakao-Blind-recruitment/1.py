def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        tmp = bin(tmp)[2:]
        tmp = tmp.zfill(n)
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        result.append(tmp)

    return result