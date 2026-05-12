class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        majority_count = len(nums)//3
        num_counter = Counter(nums)
        for num,count in num_counter.items():
            if count > majority_count:
                output.append(num)
        return output        