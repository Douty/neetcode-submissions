class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        vector<int> copy = nums;
        for (int i = 0; i < nums.size(); i++)
        {
            copy.push_back(nums[i]);
        }
        
        return copy;
    }
};