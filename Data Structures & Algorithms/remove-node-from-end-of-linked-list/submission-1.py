# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        #always use dummy in deletion ll qs for edge case
        dummy = ListNode(0, head)
        cur = head
        while cur:
            cur = cur.next
            length+=1
        
        cur = dummy
        #want to access node prior to removal node. 
        #check edge case of final node
        for i in range(length - n):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next
