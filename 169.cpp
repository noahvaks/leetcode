// 169. Majority Element

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // sort the array
        sort(nums.begin(), nums.end());
        //find and return the middle element
        int mid = nums.size()/2;
        return nums[mid];
    }
};
