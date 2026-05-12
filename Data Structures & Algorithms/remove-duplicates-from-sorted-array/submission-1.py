class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        unique = len(nums_sorted)
        nums[:unique]=nums_sorted
        return unique


        