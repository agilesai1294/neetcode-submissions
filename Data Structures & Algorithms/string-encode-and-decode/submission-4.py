class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+'#'+word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        left = right = 0
        result = []
        while right < len(s):
            left = right
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right+1
            right = left+length
            word = s[left:right]
            result.append(word)
        return result
