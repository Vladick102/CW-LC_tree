class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not node:
        return []

    res = [node]
    c = 0
    while c < len(res):
        n = res[c]

        if n.left:
            res.append(n.left)
        if n.right:
            res.append(n.right)
        c += 1

    return [i.value for i in res]
