import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        output = []
        for num,count in num_counter.items():
            heapq.heappush(output, (count,num))
            if len(output) > k:
                heapq.heappop(output)
        result = []
        for count, num in output:
            result.append(num)
        return result

        
        