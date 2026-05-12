class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        result = []
        
        for num,count in counter.items():
            heapq.heappush(result, (count,num))
        n = len(result)
        for i in range(n-k):
            heapq.heappop(result)
    
        output = []
        while len(result) != 0:
            value = heapq.heappop(result)
            output.append(value[1])

        return output
        