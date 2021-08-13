from collections import deque


def solution(cacheSize, cities):
    if cacheSize <= 0:
        return len(cities) * 5

    cache = deque([])

    access_time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            access_time += 1
            cache.remove(city)

        # cache 에 없고, cache가 꽉참 -> replacement
        elif len(cache) >= cacheSize:
            access_time += 5
            cache.popleft()
        # cache 에 없지만, cache가 비어있음
        else:
            access_time += 5

        cache.append(city)

    return access_time