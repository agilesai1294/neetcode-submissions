class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIndex = {}
        for index,num in enumerate(nums):
            require_target = target-num
            if require_target in mapIndex:
                return sorted([index,mapIndex[require_target]])
            mapIndex[num] = index
        return []        