# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
           return None
        current = head
        lst1 = []
        i = 1
        while current and i<left:
            i +=1
            lst1.append(current)
            current = current.next
        lst2 = []
        
        while current and (i>=left and i<=right): 
            i+=1
            lst2.append(current)
            current = current.next
        lst2.reverse()
        lst3 = []
        while current and i>right:
            i+=1
            lst3.append(current)
            current = current.next

        lst = lst1 + lst2 + lst3
        head = lst[0]
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[len(lst)-1].next = None
        return head
        
        
        