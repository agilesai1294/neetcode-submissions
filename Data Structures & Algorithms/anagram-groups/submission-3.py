class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = {}
        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word in output:
        #         output[sorted_word].append(word)
        #     else:
        #         output[sorted_word]=[word]
        # return list(output.values())
        output = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)- ord('a')] += 1
            output[tuple(count)].append(word)
        return list(output.values())