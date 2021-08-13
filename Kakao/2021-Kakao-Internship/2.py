def find_people_list(place):
    result = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                result.append((i, j))

    return result


def is_dist1_people(place, location):
    # 맨해튼 거리 == 1 인 move
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    result = False
    x, y = location[0], location[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= 4 and 0 <= ny <= 4 and place[nx][ny] == 'P':
            result = True

    return result


def find_dist2_people(place, location):
    # 맨해튼 거리 == 2 인 move 8개
    dx = [-2, -1, -1, 0, 0, 1, 1, 2]
    dy = [0, -1, 1, -2, 2, -1, 1, 0]

    result = []
    x, y = location[0], location[1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= 4 and 0 <= ny <= 4 and place[nx][ny] == 'P':
            result.append((nx, ny))

    return result


def is_block(place, location1, location2):
    # 맨하튼 거리 == 2인 경우만 location으로 들어옴
    dx = location2[0] - location1[0]
    dy = location2[1] - location1[1]

    is_blocked = False

    if abs(dx) == 1 and abs(dy) == 1:
        x, y = location1[0], location1[1]
        if place[x + dx][y] == 'X' and place[x][y + dy] == 'X':
            is_blocked = True
    else:
        if abs(dx) == 2:
            nx = (location1[0] + location2[0]) // 2
            ny = location1[1]
        else:
            nx = location1[0]
            ny = (location1[1] + location2[1]) // 2

        if place[nx][ny] == 'X':
            is_blocked = True

    return is_blocked


def solution(places):
    result = []
    for place in places:
        people = find_people_list(place)

        # 대기실에 사람이 없는 경우: 거리두기 지킴
        if not people:
            result.append(1)
            continue

        is_far_enough = True
        for person in people:
            # 거리 == 1 에 사람이 있는 경우: 거리두기 안지킴
            if is_dist1_people(place, person):
                is_far_enough = False
                break

            adj_people_list = find_dist2_people(place, person)

            # 거리 <= 2 사람이 없는 경우: 거리두기 지킴
            if not adj_people_list:
                continue

            is_blocked_all = True  # 플래그
            for adj_person in adj_people_list:
                # 거리 == 2 인 사람이 파티션으로 막혀있지 않은 경우 
                if not is_block(place, person, adj_person):
                    is_blocked_all = False
                    break

            # 파티션으로 막혀 있지 않은 경우: 거리두기 안지킴
            if not is_blocked_all:
                is_far_enough = False
                break

        # 충분히 멀거나 막혀있으면: 거리두기 지킴
        if is_far_enough:
            result.append(1)
        else:
            result.append(0)

    return result
