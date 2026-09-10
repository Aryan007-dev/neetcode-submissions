# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        qu = deque()
        if root:
            qu.append(root)
        while qu:
            level=[]
            for _ in range(len(qu)):
                node = qu.popleft()
                level.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right) 
            order.append(level)       

        return order        