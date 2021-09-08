import sys

sys.setrecursionlimit(10 ** 8)


class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.num)


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, node):  # 이부분 레벨 다르게 자식 노드 들어오는 경우 에러 가능 생각
        if not self.root:
            self.root = node
            return

        now = self.root
        while True:
            if now.x < node.x:
                if not now.right:
                    now.right = node
                    break
                now = now.right

            else:
                if not now.left:
                    now.left = node
                    break
                now = now.left

    def preorder(self):
        result = []

        def preorder_(node):
            if node == None:
                return
            result.append(node.num)
            preorder_(node.left)
            preorder_(node.right)

        preorder_(self.root)
        return result

    def postorder(self):
        result = []

        def postorder_(node):
            if node == None:
                return
            postorder_(node.left)
            postorder_(node.right)
            result.append(node.num)

        postorder_(self.root)
        return result


def solution(nodeinfo):
    # b-graph 만들기
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    # (-y, -x)로 정렬
    nodeinfo.sort(key=lambda x: (-x[1], -x[0]))

    # 트리 만들기
    x, y, num = nodeinfo[0]
    node = Node(num, x, y)
    tree = Tree(node)

    # 누가 부모인지 판단 -> 잠깐 미뤄두고 그냥 트리에서 판단해서 한번 넣어주는 것 시도
    for i in range(1, len(nodeinfo)):
        x, y, num = nodeinfo[i]
        node = Node(num, x, y)
        tree.insert(node)

    # 탐색하기
    result = []
    result.append(tree.preorder())
    result.append(tree.postorder())

    answer = [[]]
    return result