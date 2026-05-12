class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                current_length = 1
                while (num+current_length) in numset:
                    current_length += 1
                longest = max(longest,current_length)
        return longest
        
            


        
        