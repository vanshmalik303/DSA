# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def bst(root):
            if root is None:
                return 
            bst(root.left)
            result.append(root.val)
            bst(root.right)
        bst(root)
        return result