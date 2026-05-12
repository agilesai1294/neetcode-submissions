class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+'#'+word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left +length
            word = s[left:right]
            output.append(word)
            left = right
        return output