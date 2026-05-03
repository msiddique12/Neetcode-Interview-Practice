# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1
        
        #takes care of [] [] and [][1] and [1][]
        #dummy node
        dummy = ListNode()
        cur1 = list1
        cur2 = list2

        nc = dummy
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                nc.next = cur1
                cur1 = cur1.next
            else:
                nc.next = cur2
                cur2 = cur2.next
            nc = nc.next
        if cur1:
            nc.next = cur1
        if cur2:
            nc.next = cur2
        
        return dummy.next



