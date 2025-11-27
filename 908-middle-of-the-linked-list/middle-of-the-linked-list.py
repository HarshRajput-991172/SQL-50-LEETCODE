# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = 0 
        temp = head
        #count node
        while temp is not None:
            n += 1
            temp = temp.next
        temp = head
        # traverse the middle of list  
        for i in range(n//2):
            temp = temp.next
        return temp  

    