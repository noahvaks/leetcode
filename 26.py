# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

# Return k.

#i think this is saying that i can swap a redundant value with the next value. to do this i need a pointer to the index of the value to be replaced and the index of the next value to be inserted. 

# i can have a while loop the size of the array. 'next' increments at every loop, 'current' is flagged when a duplicate is found. once 'current' is dropped, when i find a new value i swap its value with the one at the current index.

# i think what i want to do check where a value is not greater than the previous value, and from there try to have the array increase. it should always be increasing, so i'll have a check that the current value is greater than the previous, is not, i'll look AHEAD to grab the next value and bring it in. that value is my while loop, which will run until we hit the last index. 

#it looks like i was forgetting the counter of unique values. i could instead count the number of unique values while looping through the array. technically the amount of unique values-1 should also be the index where i add the next new value. i know it's new if if the current value doesn't equal the previous. we know the array will always 1 or greater

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        return k

                


            
            
            
            


        
