from collections import deque


class Truck:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end


def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    q = deque()
    in_truck = Truck(truck_weights[0], 1, bridge_length)
    out_truck = in_truck  # out_truck 초기화
    q.append(in_truck)

    weight_in_bridge = truck_weights[0]
    n_truck_in_bridge = 1
    current_time = 1

    for i in range(1, n):
        print(q[-1].weight, q[-1].start, q[-1].end)
        # 다리 길이가 꽉 찬 경우
        if n_truck_in_bridge >= bridge_length:
            out_truck = q.popleft()
            weight_in_bridge -= out_truck.weight
            n_truck_in_bridge -= 1

        # 트럭이 다리에 없는 경우
        if not q:
            current_time = out_truck.end + 1
            in_truck = Truck(truck_weights[i], current_time, current_time + bridge_length - 1)
            q.append(in_truck)
            weight_in_bridge += in_truck.weight
            n_truck_in_bridge += 1
            continue

        # 트럭을 내보내는 경우
        while current_time > q[0].end:
            out_truck = q.popleft()
            weight_in_bridge -= out_truck.weight
            n_truck_in_bridge -= 1

        # 다름 트럭이 바로 들어갈 수 있는 경우
        if weight_in_bridge + truck_weights[i] <= weight:
            current_time = q[-1].start + 1
            in_truck = Truck(truck_weights[i], current_time, current_time + bridge_length - 1)
            q.append(in_truck)
            weight_in_bridge += in_truck.weight
            n_truck_in_bridge += 1
            continue

        # 다리 무게가 꽉찬 경우
        while weight_in_bridge + truck_weights[i] > weight:
            out_truck = q.popleft()
            weight_in_bridge -= out_truck.weight
            n_truck_in_bridge -= 1

        current_time = out_truck.end + 1
        in_truck = Truck(truck_weights[i], current_time, current_time + bridge_length - 1)
        q.append(in_truck)
        weight_in_bridge += in_truck.weight
        n_truck_in_bridge += 1

    print(q[-1].weight, q[-1].start, q[-1].end)

    answer = q[-1].end + 1
    return answer


case1 = solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1])
case2 = solution(10000, 10000, [1, 2, 3, 4, 5, 6, 7, 5000])
case3 = solution(10, 10, [7, 2, 1, 9])
case4 = solution(1, 10, [2, 3, 4, 5])
print(case1)
print(case2)
print(case3)
print(case4)
