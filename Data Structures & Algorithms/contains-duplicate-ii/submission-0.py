class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        index1, index2 = -1, -1
        for i in range(len(nums)):
            if nums[i] in indexMap:
                index1 = i
                index2 = indexMap[nums[i]]
                if abs(index2-index1) <= k:
                    return True
            indexMap[nums[i]] = i
        return False
                