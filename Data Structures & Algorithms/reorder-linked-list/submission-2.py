# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

        #Solution recursion
        # def rec(root: ListNode, cur: ListNode) -> ListNode:
        #     if not cur:
        #         return root
            
        #     root = rec(root, cur.next)

        #     if not root:
        #         return None
            
        #     tmp = None
        #     if root == cur or root.next == cur:
        #         cur.next = None
        #     else:
        #         tmp = root.next
        #         root.next = cur
        #         cur.next = tmp
            
        #     return tmp

        # head = rec(head, head.next)

        #solution 1 - O(n)
        # nodes = []

        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next
        
        # i, j = 0, len(nodes) - 1
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i+=1
        #     if i >=j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j-=1

        # nodes[i].next = None
