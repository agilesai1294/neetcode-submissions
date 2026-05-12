class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element_count = len(nums)//2
        num_counter = Counter(nums)
        for num,count in num_counter.items():
            if count >= majority_element_count:
                return num
        return -2
        