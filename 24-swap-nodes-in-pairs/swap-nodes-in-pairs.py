# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            next_curr = curr.next

            # Save the next pair
            curr.next = next_curr.next

            # Swap
            next_curr.next = curr
            prev.next = next_curr

            # Move pointers
            prev = curr
            curr = curr.next

        return dummy.next