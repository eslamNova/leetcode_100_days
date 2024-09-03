# O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while(head):
            li.append(head.val)
            head = head.next
            
        if len(li) > 0:
            for n in li:
                new_node = ListNode(n)
                if head is None:
                    head = new_node
                else:
                    new_node.next = head
                    head = new_node
                
            return new_node
        else:
            return head
        
        
        