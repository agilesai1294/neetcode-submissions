class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = dict(Counter(nums).most_common())
        output = []
        for num, count in num_counter.items():
            if len(output) < k and num not in output:
                output.append(num)
        return output

        