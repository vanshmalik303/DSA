# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        head3 = l2
        first = []
        second = []
        while head1 :
            first.append(head1.val)            
            head1 = head1.next

        while head2 :
            second.append(head2.val)
            head2 = head2.next
   

        sum1 = int(''.join(map(str,first[::-1]))) if first else 0
        sum2 = int(''.join(map(str,second[::-1]))) if second else 0
        plus = sum1+sum2
        lst = list(map(int,str(plus)))[::-1]

        tempnode = ListNode(0)
        curr = tempnode

        for i in lst:
            curr.next = ListNode(i)
            curr = curr.next
        return tempnode.next
