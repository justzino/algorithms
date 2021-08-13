NOTATION = '0123456789ABCDEF'


def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]

    if not q:
        return n

    return numeral_system(q, base) + n


def solution(n, t, m, p):
    max_x = t * m
    # n진법 max_x번째 숫자가 속한 수열까지 구하기
    n_num, len_num, last = 1, 0, 0  # 구한 숫자 갯수, 현재 수열 길이, 마지막 숫자
    while True:
        len_num += 1
        n_next = (n - 1) * (n ** (len_num - 1)) * len_num

        if n_num + n_next > max_x:
            last = n ** (len_num - 1) + ((max_x - n_num) // len_num)
            break
        else:
            n_num += n_next

    # 구한 수열까지의 수를 n진법으로 바꿔서 나열
    nums = [numeral_system(i, n) for i in range(last + 1)]
    nums = ''.join(nums)

    # 튜브의 순서에 맞춰 문자열로 구하기
    answer = nums[p - 1:max_x:m]

    return answer


"""
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p

구해야하는 수의 개수 = t * m
"""