# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findsucc(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root.val


    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return 
        if root.val<key:
            root.right =  self.deleteNode(root.right,key)
        elif root.val>key:
            root.left =  self.deleteNode(root.left,key)

        else :
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                succ = self.findsucc(root)
                root.val = succ
                root.right = self.deleteNode(root.right,succ)
        return root