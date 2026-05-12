class Solution:
    def numBits(self,n:int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.numBits(i))
        return res
        