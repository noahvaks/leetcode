# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        c = 0
        # go through the array and test on each, adding to hash table if not found
        for i in range(len(nums)):
            c = target - nums[i]
            if c in d:
                return [d[c],i]
            d[nums[i]] = i 
        
