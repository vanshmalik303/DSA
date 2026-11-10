# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
            dummy = ListNode(0)
            dummy.next = head

            prev = dummy
            curr = head

            while curr and curr.next:
                if curr.val == curr.next.val:
                    while curr.next and curr.val == curr.next.val:
                        curr = curr.next

                    prev.next = curr.next
                    curr = curr.next

                else:
                    prev = curr
                    curr = curr.next

            return dummy.next