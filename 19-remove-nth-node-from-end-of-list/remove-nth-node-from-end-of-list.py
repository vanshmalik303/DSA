# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        count2 = 0
        first = head
        second = head
        
        # if head and head.next == None:
        #     return -1

        while first != None:
            count +=1
            first = first.next
        print(count)
        target = count-n
        if target == 0:
            return head.next
        while second and second.next != None:
            count2+=1
            if count2 ==target:
                second.next = second.next.next
            second = second.next

        return (head)