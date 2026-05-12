# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = dummy = ListNode(0, head)
        currNode = head
        for i in range(n):
            currNode = currNode.next
        
        while currNode:
            left = left.next
            currNode = currNode.next
        
        left.next = left.next.next
        return dummy.next
        
        