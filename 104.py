# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# i want to travel down a tree until i hit the end. i count up each time.
# i have the self value, a right, and a left. i could pick left until i run out of options and then backtrack to the next right
#i'd say while both left and right don't equal 0, if i hit the end of a left i go i-- until there is a right to travel down
#if i do hit the end then i store the value in an array

#i am going to try a hash map where i store a pointer to the node along with the current count
#from here i don't know how to go backwards though. i doesn't map neatly to the map index

#i think a better option would be to have a stack. i'll keep track of i too and map it to a j for max depth
#i have to loop while some condition. i can say that once the stack is empty, I have exhausted all of my options
# i,j,d[],while d is not empty

#my default action is going left. once i hit a stopping point i check i to j. then i go up until i can find a path right. i know that i'm out of spots to check when:
#do i have to store when something is visited? i think i need a flag for when something has been visited, so i can't just pop something out of a stack.  

#i figured out in order traversal but that doesn't quite let me keep track of level.

#i'm going to try this queue based level order traversal i found online
#that worked. i go through one level at a time and add all the children at that level. then i increment my level value by 1. i do this by keeping track of how big my queue is at the start of each iteration. this is the size of that level. then i add children and pop out the parents


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None: return 0
        d = [root]
        j = 0

        while d:
            l = len(d)        
            for i in range(l):
                b = d[0]
                d.pop(0)
                if b.left != None: d.append(b.left)
                if b.right != None: d.append(b.right)
            j+=1
            
        return j

        
