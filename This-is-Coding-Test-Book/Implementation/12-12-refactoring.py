def possible(answer):
    for x, y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False

        # 보인 경우
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    result = []

    for frame in build_frame:
        x, y, stuff, op = frame      # 좌표 x, y, 구조물 종류 stuff(0:기둥, 1: 보), 설치 여부 op(0:삭제, 1:설치)

        # 설치 하는 경우
        if op == 1:
            result.append([x, y, stuff])
            if not possible(result):
                result.remove([x, y, stuff])

        # 삭제 하는 경우
        if op == 0:
            result.remove([x, y, stuff])
            if not possible(result):
                result.append([x, y, stuff])

    result.sort()
    return result
