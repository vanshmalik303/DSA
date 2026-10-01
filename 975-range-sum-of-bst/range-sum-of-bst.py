# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        result = 0
        def inorder(root):
            nonlocal result
            if root is None:
                return None

            inorder(root.left)
            if root.val >= low and root.val <= high :
                result +=root.val
            inorder(root.right)
            
        inorder(root)
        return result

        