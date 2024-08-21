// 80. Remove Duplicates from Sorted Array II

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        if (nums.size() < 2) //for cases with small arrays
            return nums.size();

        int k = 2; // number of unique values
        for (int i = 2; i < nums.size(); i++){ //loop through array
          if (nums[i] != nums[k-2]) // if value is not yet seen twice
          {
              nums[k] = nums[i]; // replace in array at index of amt of unique values
              k++; // increase # of values
          }
        }
        return k;
        
    }
};
