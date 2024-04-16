# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        lst = []
        while current:
            if current in lst:
                return True
            lst.append(current)
            current = current.next
            
        return False
        
        
        
        