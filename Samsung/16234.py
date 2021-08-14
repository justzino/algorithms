class Country:
    def __init__(self, population: int, x: int, y: int):
        self.population = population
        self.location = [x, y]
        self.is_union = False
        self.alliance_num = None

    def add_to_union(self, alliance_number: int):
        self.alliance_num = alliance_number
        self.is_union = True

    def remove_from_union(self):
        self.alliance_num = None
        self.is_union = False

    def adj_loc(self, n) -> list:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = self.location[0], self.location[1]
        result = []

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            else:
                result.append([nx, ny])
        return result


class Alliance:
    def __init__(self, number):
        self.countries = set()
        self.number = number

    def add(self, country: Country):
        self.countries.add(country)
        country.add_to_union(self.number)

    def remove(self, country: Country):
        self.countries.remove(country)
        country.remove_from_union()


def check_p_gap(c1: int, c2: int) -> bool:
    if MIN_GAP <= abs(c1 - c2) <= MAX_GAP:
        return True
    return False


if __name__ == "__main__":
    N, MIN_GAP, MAX_GAP = map(int, input().split())
    countries = list()  # [Country1, Country2, ...]
    alliances = dict()   # [set(), set(), ...] => [동맹1, 동맹2, ...]
    i_last_union = 0
    days = 0

    # 입력 받기
    for i in range(N):
        input_line = list(map(int, input().split()))
        countries_by_line = []

        # Country 초기화
        j = 0
        for population in input_line:
            countries_by_line.append(Country(population, i, j))
            j += 1
        countries.append(countries_by_line)

    # open 될 국경이 있으면
    while True:
        # 모든 나라의 인접 나라간 인구차 확인 -> 범위 내이면 alliance 에 union
        for i in range(N):
            for j in range(N):
                now = countries[i][j]
                for x, y in now.adj_loc(N):
                    # 인구 차이가 범위 내이면 두 나라 union
                    adj = countries[x][y]
                    if check_p_gap(now.population, adj.population):
                        if now.is_union:
                            alliance = Alliance(i_last_union)
                            alliances.append(alliance)
                            alliances[now.alliance_num].add(adj)
                            adj.add_to_union(now.alliance_num)
                        else:
                            alliance.append({now, adj})
                            now.add_to_union(i_last_union)
                            adj.add_to_union(i_last_union)
                            i_last_union += 1
        # 모든 alliance 인구 분배 -> alliance 가 없으면 끝
        if not alliance:
            break
        while alliance:
            now_alliance = alliance.pop()
            sum_population = 0
            for country in now_alliance:
                sum_population += country.population
            avg_population = sum_population // len(now_alliance)

            for country in now_alliance:
                country.population = avg_population

        days += 1

    print(days)

"""
L <= 인구차이 <= R? 두 나라 사이 국경선 open
열어야하는 국경선이 모두 Open? 인구 이동 start
인접한 칸만 이용해 이동 가능? 그 나라 => 연합(union)
union을 이루는 각 칸의 인구수 = (연합 인구수) / (연합을 이루는 칸의 개수) => 소수점 버림
union 해제, 국경선 close


print(인구 이동이 발생한 일수)
"""
