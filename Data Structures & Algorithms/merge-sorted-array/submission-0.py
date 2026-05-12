class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1index = m-1
        num2index = n-1
        for i in range(n+m-1,-1,-1):
            if num2index < 0:
                break
            if num1index >= 0 and nums1[num1index] > nums2[num2index]:
                nums1[i] = nums1[num1index]
                num1index -= 1
            else:
                nums1[i] = nums2[num2index]
                num2index -= 1
        

        