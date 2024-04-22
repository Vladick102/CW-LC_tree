# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        head = root
        while head:
            if (head.right and head.right.val == key) or (
                head.left and head.left.val == key
            ):

                if head.left and head.left.val == key:
                    temp = head.left
                else:
                    temp = head.right

                if temp.left is None and temp.right is None:
                    if temp == head.right:
                        head.right = None
                    else:
                        head.left = None
                    break

                elif temp.left and temp.right:
                    subtree = temp.left
                    while subtree.right:
                        subtree = subtree.right
                    subtree.right = temp.right
                    temp.right = None

                    if head.left and head.left.val == key:
                        head.left = temp.left
                        temp = None

                    elif head.right and head.right.val == key:
                        head.right = temp.left
                        temp = None
                    break

                elif temp.left:
                    if temp == head.right:
                        head.right = temp.left
                    else:
                        head.left = temp.left
                    break

                elif temp.right:
                    if temp == head.right:
                        head.right = temp.right
                    else:
                        head.left = temp.right
                    break

            elif head.val == key:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                subtree = root.left
                while subtree.right:
                    subtree = subtree.right

                subtree.right = root.right
                return root.left

            if head.val > key:
                head = head.left
            elif head.val < key:
                head = head.right
            else:
                return 1

        return root
