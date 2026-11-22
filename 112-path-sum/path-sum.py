# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def bst(root, ans):
            if root is None:
                return False

            ans += root.val

            if root.left is None and root.right is None:
                return ans == targetSum

            return bst(root.left, ans) or bst(root.right, ans)

        return bst(root, 0)
