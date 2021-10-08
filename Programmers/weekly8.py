def solution(sizes):
    long = 0
    short = 0

    for size in sizes:
        if size[0] >= size[1]:
            long = max(long, size[0])
            short = max(short, size[1])
        else:
            long = max(long, size[1])
            short = max(short, size[0])

    answer = long * short
    return answer
