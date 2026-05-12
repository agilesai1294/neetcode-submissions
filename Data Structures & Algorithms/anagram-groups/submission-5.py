class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            sorted_strs[tuple(count)].append(word)
        return list(sorted_strs.values())
        