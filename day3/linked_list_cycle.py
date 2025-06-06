# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head

        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast = fast.next.next
            if( slow==fast):
                return True
        
        return False
        
S = Solution()
S.hasCycle([3,2,0-4])