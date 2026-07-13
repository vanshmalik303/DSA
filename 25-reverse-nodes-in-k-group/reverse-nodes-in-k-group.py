# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        count1 = 0
        while temp and count1<k :
            temp = temp.next
            count1+=1

        if count1<k:
            return head

        prev = None
        curr = head
        count2 = 0 
        while curr and count2<k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count2+=1

        head.next = self.reverseKGroup(curr,k)

        return prev