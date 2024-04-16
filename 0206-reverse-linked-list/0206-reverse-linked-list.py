# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head
        
        if head == None:
            return None
        lst = []
        while currentNode:
            lst.append(currentNode)
            currentNode = currentNode.next
        lst.reverse()
        
        head = lst[0]
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[len(lst)-1].next = None
        return head
        


        
    
            
        
        
            
                
                
                
                    
        #         lst.append(node.val)
        #         node = node.next
        # return lst.reverse()           

        
          
        