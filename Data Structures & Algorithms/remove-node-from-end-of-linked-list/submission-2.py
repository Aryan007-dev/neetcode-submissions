# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end=1
        c = head
        p = None 
        while c and c.next:
            c = c.next
            end+=1
            
        c = head
        idx = (end - n)
        if idx == 0:
            return head.next  
        i = 0
        while i!=idx:
            p = c
            c = c.next
            
            i+=1
        p.next = c.next
        return head    
    


            
            

        