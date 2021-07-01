import re

priorities = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]


def calc(nums, ops):
    result = []

    for operators in priorities:
        _nums = nums[:]
        _ops = ops[:]

        for op in operators:
            while op in _ops:
                idx = _ops.index(op)
                value = str(eval(_nums[idx] + _ops[idx] + _nums[idx + 1]))
                _nums[idx] = value
                _nums = _nums[:idx+1] + _nums[idx+2:]
                _ops = _ops[:idx] + _ops[idx+1:]

        result.append(abs(int(_nums[0])))

    answer = max(result)
    return answer


def solution(expression):
    op_pattern = re.compile('[*+-]')
    nums = op_pattern.split(expression)
    ops = op_pattern.findall(expression)

    result = calc(nums, ops)

    return result
