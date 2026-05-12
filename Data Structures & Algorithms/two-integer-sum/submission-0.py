class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for i, num in enumerate(nums):
            required_target = target-num
            if required_target in mapIndex:
                return sorted([i, mapIndex[required_target]])
            mapIndex[num] = i
        return []
        