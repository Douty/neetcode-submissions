class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum  = 1 
        p_arr = [0] * len(nums)

        for i in range(len(nums)):
            p_arr[i] = pre_sum
            pre_sum *= nums[i]

        suf_sum = 1
        suf_arr = [0] * len(nums)
        for j in range(len(nums) -1, -1,-1):
            suf_arr[j] = suf_sum
            suf_sum *= nums[j]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = p_arr[i] * suf_arr[i]

        return res