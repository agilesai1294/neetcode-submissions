class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = float('-inf')
        for right, num in enumerate(nums):
            if num-1 not in numset:
                length = 1
                while num+length in numset:
                    length += 1
                max_length = max(max_length, length)
        return max_length if max_length != float('-inf') else 0
 
        