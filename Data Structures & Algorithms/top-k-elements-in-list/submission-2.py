class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        # sorting dictionary by values in descending order
        num_counter_des = dict(Counter(nums).most_common())
        output = []
        for num,count in num_counter_des.items():
            if len(output) < k:
                if num not in output:
                    output.append(num)
        return output