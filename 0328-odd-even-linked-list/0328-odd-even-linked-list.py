# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    
        current = head
        lst = []
        
        while current:
            lst.append(current)
            current = current.next
        n = len(lst)
        if n == 0:
            return None
        if n == 1 or n == 2:
            return head
        odd = [x for x in lst if (lst.index(x)%2 == 0)]
        even = [x for x in lst if (lst.index(x)%2 != 0)]
        lst = odd + even
        
        head = lst[0]
        
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[len(lst) - 1].next = None
        return head
        


        