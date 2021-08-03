from collections import deque

DUMMY_TRUCK = 0


class Bridge:

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = deque()
        self._current_weight = 0

    def push(self, truck_weight) -> bool:
        next_weight = self._current_weight + truck_weight
        # 다리가 꽉찬 경우
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck_weight)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        truck_weight = self._queue.popleft()
        self._current_weight -= truck_weight

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    time = 0
    # 트럭이 전부 다리에 진입
    while trucks:
        print(bridge)
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        time += 1

    # 트럭이 전부 다리에서 나옴
    while bridge:
        bridge.pop()
        time += 1

    return time


def main():
    case1 = solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1])
    # case2 = solution(10000, 10000, [1, 2, 3, 4, 5, 6, 7, 5000])
    case3 = solution(10, 10, [7, 2, 1, 9])
    case4 = solution(1, 10, [2, 3, 4, 5])
    print(case1)
    # print(case2)
    print(case3)
    print(case4)


if __name__ == '__main__':
    main()