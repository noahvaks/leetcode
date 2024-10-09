# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        
        while curr:
            temp = curr.next #the actual next one
            curr.next = prev #change to now point backwards
            prev = curr # move forward
            curr = temp # move forward
            
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can just traverse the list and add the current node to the head of a new list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        if curr:
            newHead = ListNode()
            newHead.val = curr.val

            while curr:
                curr = curr.next
                if curr:
                    newNode = ListNode(curr.val)
                    newNode.next = newHead
                    newHead = newNode
                    
            return newHead
        return None

        

        
