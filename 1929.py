# 1929. Concatenation of Array

#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# 1 <= n <= 1000

#i'm adding an array on top of itself
# so i go through a loop the length of the array once where i set the value at i and i+len ?

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums) * 2
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[len(nums) + i] = nums[i]
        
        return ans
