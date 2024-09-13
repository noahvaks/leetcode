# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if

# there are two distinct indices i and j in the array such that nums[i] == nums[j]
#loop through array, add number and list of indices


# and abs(i - j) <= k.
#loop through indices and test case


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        #create map
        d = {} 
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]] += [i]
        
        #check for abs(i - j) <= k.
        for y in d.values():
            if len(y) > 1:
                j=1
                i=0
                while j < len(y):
                    if (abs(y[i] - y[j]) <= k):
                        return True
                    j+=1
                    i+=1
        return False

