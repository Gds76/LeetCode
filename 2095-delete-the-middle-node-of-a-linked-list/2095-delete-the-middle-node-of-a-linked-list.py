# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        current = head
        lst = []
        
        while current:
            lst.append(current)
            current = current.next
        n = len(lst)//2
        lst.remove(lst[n])
        if len(lst) == 0:
            return None
        head = lst[0]
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[len(lst)-1].next = None
        return head

