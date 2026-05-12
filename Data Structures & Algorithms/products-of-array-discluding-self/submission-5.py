class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = [1]*len(nums)
        for i, num in enumerate(nums):
            result[i] = prefix
            prefix = prefix*num
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i]*postfix
            postfix = postfix*nums[i]
        return result
        