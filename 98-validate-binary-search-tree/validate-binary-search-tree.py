# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def bst(root,low,hi):

            if root is None:
                return True
            
            if root.val<=low or root.val>=hi:
                return False
            
            return bst(root.left,low,root.val) and bst(root.right,root.val,hi)
        return bst(root,float('-inf'),float('inf'))
