// 27. Remove Element

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int vals = 0;
        for (int i = 0; i < nums.size(); i++) {
            //if value is valid
            if (nums[i] != val) {
            //set value at valid position in new array
                nums[vals] = nums[i];
            //go up by 1 in new array index
                vals++;
                }
            }
        // return number of valid elements in nums
        return vals;
    }
};
