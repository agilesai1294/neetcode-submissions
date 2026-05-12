class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        output = ""
        for i in range(min(len(sorted_strs[-1]), len(sorted_strs[0]))):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                output += sorted_strs[0][i]
            else:
                break
        return output
        