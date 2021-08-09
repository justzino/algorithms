class Number:
    def __init__(self, value: str):
        self.value = value

    def __lt__(self, other):
        num1 = self.value + other.value
        num2 = other.value + self.value

        if num1 < num2:
            return True

        return False

    def __repr__(self):
        return self.value


def solution(numbers):
    numbers = [Number(str(num)) for num in numbers]
    numbers.sort(reverse=True)
    numbers = list(map(str, numbers))

    answer = ''.join(numbers)

    while answer[0] == '0' and len(answer) > 1:
        answer = answer[1:]

    return answer


if __name__ == '__main__':
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
    # print(solution())
    # print(solution())

