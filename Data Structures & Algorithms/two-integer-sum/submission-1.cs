public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> seen = new();

        for (int i = 0; i < nums.Length; i++)
        {
            int comp = target - nums[i];
            if (seen.ContainsKey(comp))
            {
                seen.TryGetValue(comp, out int idx);
                return [idx,i];
            }
            seen[nums[i]] = i;
        }
        return [];
    }
}
