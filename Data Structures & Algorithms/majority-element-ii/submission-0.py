class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_element_count = len(nums)//3
        nums_counter = Counter(nums)
        output = []
        for num,count in nums_counter.items():
            if count > majority_element_count:
                output.append(num)
        return output
        