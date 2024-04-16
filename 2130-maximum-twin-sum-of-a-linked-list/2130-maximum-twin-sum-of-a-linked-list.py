# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        current = head
        
        
        while current:
            lst.append(current.val)
            current = current.next
        n = len(lst)
        
        lst1 = []
        for i in range(len(lst)):
            
            lst1.append(lst[i] + lst[n-1-i])
        return max(lst1)


        

        