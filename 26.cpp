// 26. Remove Duplicates from Sorted Array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int k = 1; // number of unique values
        for (int i = 1; i < nums.size(); i++){ //loop through array
            if (nums[i] != nums[k-1]) // if value is not yet seen
            {
                nums[k] = nums[i]; // replace in array at index of amt of unique values
                k++; // increase # of values
            }
        }
    return k;
    }
};
