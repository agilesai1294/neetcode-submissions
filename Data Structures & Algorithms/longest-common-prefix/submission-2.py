class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        firstword_len = len(sorted_strs[0])
        lastword_len = len(sorted_strs[-1])
        result = ""
        for i in range(min(firstword_len,lastword_len)):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                result += sorted_strs[0][i]
            else:
                break
        return result
        