class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        result = []
        for num,count in num_counter.items():
            heapq.heappush(result, (count,num))
            if len(result) > k:
                heapq.heappop(result)
        
        output = []
        for i in range(len(result)):
            output.append(result[i][1])

        return output
        