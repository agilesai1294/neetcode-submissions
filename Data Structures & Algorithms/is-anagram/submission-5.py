class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        for char in t:
            s_counter[char] -= 1
        
        for char,count in s_counter.items():
            if count != 0:
                return False
        return True
        