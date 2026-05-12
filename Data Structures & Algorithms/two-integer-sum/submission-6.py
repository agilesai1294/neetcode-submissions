class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for index, num in enumerate(nums):
            required_target = target-num
            if required_target in mapIndex:
                return[mapIndex[required_target], index]
            mapIndex[num] = index
        return [-1, -1]
        