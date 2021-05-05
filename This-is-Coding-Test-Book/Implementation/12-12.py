def solution(n, build_frame):
    matrix = [[[-1] * 4 for i in range(n+1)] for j in range(n+1)]   # 위, 오, 아래, 왼 연결 순서
    result = []

    def available_remove_pillar(t_x, t_y):
        # 기둥 위에 보가 없는 경우
        if matrix[t_x][t_y+1][1] != 1 and matrix[t_x][t_y+1][3] != 1:
            # 위에 보는 없지만 기둥이 있는 경우: 제거 불가능
            if matrix[t_x][t_y+1][0] == 1:
                return False
            # 위에 보, 기둥 전부 없는 경우: 제거 가능
            return True

        # 위에 보가 있고 맨 마지막 기둥인 경우: 제거 못함
        if matrix[t_x][t_y+1][1] != 1 or matrix[t_x][t_y+1][3] != 1:
            return False

        return True

    def available_remove_floor(t_x, t_y):
        # 양 옆에 보가 없는 경우
        if matrix[t_x+1][t_y][1] != 1 and matrix[t_x][t_y][3] != 1:
            return True

        # 왼쪽에 보가 있는 경우
        if matrix[t_x][t_y][3] != 1:
            if matrix[t_x][t_y][2] == 1:
                pass
            elif matrix[t_x-1][t_y][2] == 1:
                pass
            else:
                return False

        # 오른쪽에도 보가 있는 경우
        if matrix[t_x+1][t_y][1] == 1:
            if matrix[t_x+1][t_y][2] == 1:
                return True
            elif matrix[t_x+2][t_y][2] == 1:
                return True
            else:
                return False

    for frame in build_frame:
        x, y, a, b = frame      # 좌표 x, y, 구조물 종류 a(0:기둥, 1: 보), 설치 여부 b(0:삭제, 1:설치)

        # 설치 하는 경우
        if b == 1:
            # 기둥을 설치하는 경우
            if a == 0:
                # 바닥에 기둥을 설치 하는 경우
                if y == 0:
                    matrix[x][y][0] = 1
                    matrix[x][y+1][2] = 1
                    result.append([x, y, 0])

                # 보의 한쪽 끝 or 기둥 위에 기둥을 설치하는 경우
                elif matrix[x][y][1] == 1 or matrix[x][y][3] == 1 or matrix[x][y][2] == 1:
                    matrix[x][y][0] = 1
                    matrix[x][y+1][2] = 1
                    result.append([x, y, 0])

                # 전부 아닌 경우 무시
                else:
                    continue

            # 보를 설치하는 경우
            else:
                # 보는 한쪽 끝 부분이 기둥 위에 있거나
                if matrix[x][y][2] == 1 or matrix[x+1][y][2] == 1:
                    matrix[x][y][1] = 1
                    matrix[x+1][y][3] = 1
                    result.append([x, y, 1])

                # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                elif matrix[x][y][3] == 1 and matrix[x+1][y][1] == 1:
                    matrix[x][y][1] = 1
                    matrix[x+1][y][3] = 1
                    result.append([x, y, 1])

                # 전부 아닌 경우 무시
                else:
                    continue

        # 삭제 하는 경우 (b = 0)
        else:
            # 기둥을 삭제하는 경우
            if a == 0:
                if available_remove_pillar(x, y):
                    matrix[x][y][0] = -1
                    matrix[x][y+1][2] = -1
                    result.remove([x, y, 0])
                else:
                    continue

            # 보를 삭제하는 경우
            else:
                if available_remove_floor(x, y):
                    matrix[x][y][1] = -1
                    result.remove([x, y, 1])
                else:
                    continue

    # x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순하여 return 배열
    # x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
    result.sort()
    return result
