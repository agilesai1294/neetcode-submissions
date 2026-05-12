class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in mapIndex:
                return [mapIndex[req], i]
            mapIndex[num] = i
        return [-1, -1]
        