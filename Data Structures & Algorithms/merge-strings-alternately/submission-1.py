class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Len = len(word1)
        word2Len = len(word2)
        if word1Len == 0:
            return word2
        if word2Len == 0:
            return word1
        minLength = min(word1Len, word2Len)
        result = []
        for i in range(minLength):
            result.append(word1[i])
            result.append(word2[i])
        
        if word1Len == minLength:
            result.append(word2[minLength:])
        else:
            result.append(word1[minLength:])
        return ''.join(result).strip()
        