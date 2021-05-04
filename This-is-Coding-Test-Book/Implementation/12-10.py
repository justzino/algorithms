# 시계 방향으로 회전 / n: key 크기
def turn(key, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = key[i][j]

    return result


# key를 (x, y) 만큼 평행 이동, N x N 만큼 자르기 / n: lock 크기
# def move(key, x, y, lock_len):
#     result = [[0] * lock_len for _ in range(lock_len)]
#     for i in range(lock_len):
#         for j in range(lock_len):
#             try:
#                 if i+x < 0 or j+y < 0:
#                     continue
#                 result[i+x][j+y] = key[i][j]
#
#             except:
#                 continue
#
#     return result

# 값이 1인 key만 (x, y) 만큼 평행 이동, N x N 만큼 자르기 / n: lock 크기
def move(keys, key, x, y, lock_len):
    result = [[0] * lock_len for _ in range(lock_len)]
    for k in keys:
        i, j = k[0], k[1]
        try:
            if i+x < 0 or j+y < 0:
                continue
            result[i+x][j+y] = key[i][j]

        except:
            continue

    return result


# key가 lock을 풀 수 있는지 확인
def unlock(key, lock, n):
    for i in range(n):
        for j in range(n):
            if key[i][j] + lock[i][j] != 1:
                return False

    # lock + key 값이 전부 1이면 true
    return True


def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    keys, locks, gaps = [], [], []

    for c in range(4):
        # key 에서 값이 1인 부분을 lock 에서 값이 0인 부분에 맞춰서 move 하면서 모두 비교
        # lock == 0인 부분 뽑기
        for i in range(lock_len):
            for j in range(lock_len):
                if lock[i][j] == 0:
                    locks.append((i, j))

        # 예외처리: lock 이 전부 1인 경우
        if not locks:
            return True

        # key == 1인 부분 뽑기
        for i in range(key_len):
            for j in range(key_len):
                if key[i][j] == 1:
                    keys.append((i, j))

        # 예외처리: lock 에 0 이 있는데 key 가 전부 0 인 경우
        if not keys:
            return False
        
        # 예외처리: lock 0 의 개수 보다 key 1의 개수가 적은 경우
        if len(keys) < len(locks):
            return False

        # key == 1 인 부분을 lock == 0 인 부분으로 move 할 (x, y) 구하기
        for k in keys:
            for l in locks:
                gaps.append((l[0] - k[0], l[1] - k[1]))

        # 하나씩 move 시키며 비교
        for gap in gaps:
            # m_key = move(key, gap[0], gap[1], lock_len)
            m_key = move(keys, key, gap[0], gap[1], lock_len)
            result = unlock(m_key, lock, lock_len)

            if result:
                return True
            else:
                pass

        if c == 3:
            return False

        # key를 회전시켜서 다시 탐색
        key = turn(key, key_len)

