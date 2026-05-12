class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        for char,count in s_counter.items():
            if count != t_counter[char]:
                return False
        return True
        