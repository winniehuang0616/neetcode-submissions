# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root: Optional[TreeNode], arr: list()):
        arr.append(root.val)
        if root.left: self.traversal(root.left, arr)
        else: arr.append(None)
        if root.right: self.traversal(root.right, arr)
        else: arr.append(None)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = list()
        arr2 = list() 
        if p == None and q == None: return True
        if (p == None and q != None) or (p != None and q == None): return False
        self.traversal(p, arr1)
        self.traversal(q, arr2)
        if len(arr1) != len(arr2): return False
        else:
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]: return False
        return True

        