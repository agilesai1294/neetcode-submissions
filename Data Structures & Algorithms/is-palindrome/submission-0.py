class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum() or s[left] == ' ':
                left += 1
            elif not s[right].isalnum() or s[right] == ' ':
                right -= 1
            else:
                if s[right].lower() == s[left].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True
        