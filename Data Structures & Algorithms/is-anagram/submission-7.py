class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        s_count = Counter(s)
        for i in range(t_len):
            s_count[t[i]] -= 1
        
        for char, count in s_count.items():
            if count != 0:
                return False
        return True

