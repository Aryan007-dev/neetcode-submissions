"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = head
      
        d ={}
        while c:
            d[c] = Node(c.val)
            c = c.next
        c = head
        while c:
            copy = d[c]
            if c.next:
                copy.next = d[c.next]
            if c.random:
                copy.random = d[c.random ]
            c = c.next  
        return d[head] if head else None          
              
        



        
        