class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


# Pre-order traversal
def pre_order(node: Node):
    res = []

    def f(node):
        if node:
            res.append(node.data)
            if node.left:
                f(node.left)
            if node.right:
                f(node.right)
            return node.data

    f(node)
    return res


# In-order traversal
def in_order(node):
    res = []

    def f(node):
        if node:
            if node.left:
                f(node.left)
            res.append(node.data)
            if node.right:
                f(node.right)

    f(node)
    return res


# Post-order traversal
def post_order(node):
    res = []

    def f(node):
        if node:
            if node.left:
                f(node.left)
            if node.right:
                f(node.right)
            res.append(node.data)

    f(node)
    return res
