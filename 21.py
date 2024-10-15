# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
        
# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# I will loop through both lists until they both equal None
# First compare the heads and make the lower value the head of a new list
# Compare each value to each other, when one is lower add it to the new list and go next on that one
# Once I hit None I stop moving forward on that one
# i combine them by setting a new node with value i want whose next points to none. i set the CURRENT node to point to this one
#right now my code defaults to if there are equal values we push c forward

#maybe i need to change the order in which i'm setting next so i don't get stuck in a loop

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        b = list1
        c = list2
        d = ListNode()
        head = ListNode()

        #the following sets the head of the list
        if b == None and c == None: return None
        elif b == None: 
            head = ListNode(c.val,None)
            c = c.next
        elif c == None: 
            head = ListNode(b.val,None)
            b = b.next
        elif b.val < c.val: 
            head = ListNode(b.val,None)
            b = b.next
        else: 
            head = ListNode(c.val,None)
            c = c.next

        #this portion sets the list when needing to compare both values
        d = head
        while b!= None and c!= None:
            if b.val < c.val:
                newNode = ListNode(b.val,None)
                d.next = newNode
                d = d.next
                b = b.next
            else:
                newNode = ListNode(c.val,None)
                d.next = newNode
                d = d.next
                c = c.next

        # this portion fills in the remainder of the list
        while b!= None:
            newNode = ListNode(b.val,None)
            d.next = newNode
            d = d.next
            b = b.next
        while c!= None:
            newNode = ListNode(c.val,None)
            d.next = newNode
            d = d.next
            c = c.next 

        return head
        
        

            
