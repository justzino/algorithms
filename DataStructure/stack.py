class Stack:
    def __init__(self):
        self.stack = []
        self.result = []

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True

        return is_empty

    def isFull(self):
        is_full = False
        if len(self.stack) == 8:
            is_full = True

        return is_full

    def push(self, data):
        if self.isFull():
            self.result.append('Full')
        else:
            self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            self.result.append('Empty')
        else:
            pop_object = self.stack[-1]

        return pop_object
