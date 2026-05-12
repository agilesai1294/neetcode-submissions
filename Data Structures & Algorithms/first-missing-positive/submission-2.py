class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num <= 0:
            return 1
        
        numSet = set(nums)
        for i in range(1,max_num):
            if i not in numSet:
                return i
        return max_num+1