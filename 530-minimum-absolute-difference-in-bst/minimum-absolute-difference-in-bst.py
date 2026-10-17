# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        # print(ans)
        result = float('inf')
        for i in range(1,len(ans)):
            diff = abs(ans[i]-ans[i-1])
            result = min(diff,result)
        return (result)


            