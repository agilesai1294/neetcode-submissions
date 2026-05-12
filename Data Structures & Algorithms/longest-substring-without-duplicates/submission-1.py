class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        maxLength = 0
        chars = Counter()
        while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1 :
                l = s[left]
                chars[l] -= 1
                left +=1
                if chars[l] == 0:
                    del chars[l]
            maxLength = max(maxLength, right-left+1)
            right += 1
        return maxLength
        