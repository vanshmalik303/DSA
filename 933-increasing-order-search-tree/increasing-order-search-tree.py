# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        ans = []
        def inorder(root):
            nonlocal ans
            if root is None:
                return 

            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        dummy = TreeNode(0)
        curr = dummy
        for val in ans:
            curr.right = TreeNode(val)
            curr = curr.right
        return dummy.right