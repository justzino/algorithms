def solution(msg):
    dictionary = [chr(c + 65) for c in range(26)]

    n = len(msg)
    result = []

    start_ptr, finish_ptr, next_ptr = 0, 0, 0

    while start_ptr < n:
        finish_ptr = start_ptr + 1
        next_ptr = start_ptr + 1
        now = 0

        while finish_ptr <= n:
            word = msg[start_ptr:next_ptr]

            if word in dictionary:
                now = dictionary.index(word) + 1
                finish_ptr = next_ptr
                next_ptr += 1
            else:
                dictionary.append(word)
                break

        result.append(now)
        start_ptr = finish_ptr

    return result
