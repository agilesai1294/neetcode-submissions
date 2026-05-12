class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        if nums_sorted[-1] <= 0:
            return 1
        else:
            index = 1
            while index < max(nums):
                if index not in nums:
                    return index
                index += 1
            return max(nums) +1
            
        