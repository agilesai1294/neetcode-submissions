class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+'#'+word
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        right = 0
        res = []
        while right<len(s)-1:
            left = right
            while s[right] != '#':
                right += 1

            length = int(s[left:right])
            left = right+1
            right = left +length
            word = s[left:right]
            res.append(word)
        return res

