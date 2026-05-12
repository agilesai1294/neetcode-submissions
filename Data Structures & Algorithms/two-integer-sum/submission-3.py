class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for i, num in enumerate(nums):
            required_target = target-num
            if required_target in mapIndex:
                return [mapIndex[required_target],i]
            mapIndex[num] = i
        return [-1,-1]
        