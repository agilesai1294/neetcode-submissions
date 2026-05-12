class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while (num+length) in numSet:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength
        