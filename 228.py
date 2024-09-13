# 228. Summary Ranges

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

#iterate through list, store first in range
#if next-1 > 1, store next value, update first
#best way i can thin to do this is a hash map that stores the first and then the last
#and then if first = last print just that value?

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        if len(nums) > 0:
            if len(nums) == 1: #when array is too small to check these
                l.append(str(nums[0]))    
            
            first = nums[0] #for regular intervals
            for i in range(len(nums)-1):
                if nums[i+1] > nums[i] + 1:
                    if first == nums[i]:
                        l.append(str(first))
                    else:
                        l.append(("%s->%s" % (first, nums[i]))) 
                    first = nums[i+1]

                if i+2 == len(nums): #add last interval
                    if first == nums[i+1]:
                        l.append(str(first))
                    else:
                        l.append(("%s->%s" % (first, nums[i+1]))) 
            return l
            





