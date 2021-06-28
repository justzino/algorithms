from itertools import combinations


def solution(orders, course):
    result_list = [{} for _ in range(11)]

    for order in orders:
        foods = list(order)
        foods.sort()
        for i in course:
            tmp = list(map(list, combinations(foods, i)))
            for c in tmp:
                string = ''.join(c)
                try:
                    result_list[i][string] += 1
                except:
                    result_list[i][string] = 1

    answer = []
    for i in course:
        try:
            max_order = max(result_list[i].values())
            order_by_course = result_list[i]
            answer += list(
                filter(lambda x: order_by_course[x] > 1 and order_by_course[x] == max_order, order_by_course))
        except:
            continue

    answer.sort()
    return answer
