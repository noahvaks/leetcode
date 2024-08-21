# 189. Rotate Array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = k % len(nums)
        nums[0:0] = nums[len(nums)-r:]
        del nums[len(nums)-r:]
