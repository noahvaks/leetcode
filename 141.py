# 141. Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We will keep a record of visited values using a hash map. if we run into the same value we know that there is a loop.


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        b = head
        d = {}

        while b not in d:
            if b not in d:
                d[b] = 1
            if b == None:
                return False
            b = b.next

        return True
        
