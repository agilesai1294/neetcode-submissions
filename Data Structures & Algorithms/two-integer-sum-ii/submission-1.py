class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            mid = (left+right)//2
            req_target = numbers[left] + numbers[right]
            if req_target == target:
                return [left+1, right+1]
            elif req_target > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
        