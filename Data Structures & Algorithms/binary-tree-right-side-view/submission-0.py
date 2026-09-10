# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        qu = deque()
        res =[]
        if root:
            qu.append(root)
        while qu:
            n= len(qu)
            for i in range(len(qu)):
                node = qu.popleft()
                if i == n-1:
                    res.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
                        
        return res

