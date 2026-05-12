class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_s == sorted_t
        