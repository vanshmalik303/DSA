# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        ans = []
        def inorder(root):
            
            nonlocal ans
            if root is None:
                return None
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if ans[i]+ans[j]==k:
                    return True
        return False