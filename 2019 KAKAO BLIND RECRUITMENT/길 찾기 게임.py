"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42892?language=python3

"""

from sys import setrecursionlimit

setrecursionlimit(10000000)


class TreeNode:

    def __init__(self, value: int, x: int, left=None, right=None):
        self.value = value
        self.x = x
        self.left = left
        self.right = right


def solution(nodeinfo):
    nodeinfo = [[i + 1] + n for i, n in enumerate(nodeinfo)]  # (value, x, y)
    nodeinfo = sorted(nodeinfo, key=lambda i: -i[-1])  # y descending order
    root = TreeNode(nodeinfo[0][0], nodeinfo[0][1])

    def construct_tree(root, nodeinfo):
        val, x, _ = nodeinfo
        if root.x < x:
            if root.right is not None:
                construct_tree(root.right, nodeinfo)
            else:
                root.right = TreeNode(val, x)
        else:
            if root.left is not None:
                construct_tree(root.left, nodeinfo)
            else:
                root.left = TreeNode(val, x)

    # construct tree
    for i in range(1, len(nodeinfo)):
        start = root
        construct_tree(start, nodeinfo[i])

    pre_orders = []
    post_orders = []

    def preOrder(tree: TreeNode):
        if tree:
            pre_orders.append(tree.value)
            preOrder(tree.left)
            preOrder(tree.right)

    def postOrder(tree: TreeNode):
        if tree:
            postOrder(tree.left)
            postOrder(tree.right)
            post_orders.append(tree.value)

    preOrder(root)
    postOrder(root)

    return [pre_orders, post_orders]
