# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        cur  = d
        f = set(nums)
        while cur.next:

            if cur.next.val in f:
                cur.next = cur.next.next
            else:
                cur = cur.next


        return d.next

        