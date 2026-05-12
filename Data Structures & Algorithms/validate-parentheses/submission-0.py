class Solution:
    def isValid(self, s: str) -> bool:
        valid_parenthesis = {'[':']', '{':'}', '(': ')'}
        stack = []
        for char in s:
            if char in valid_parenthesis:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if valid_parenthesis[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
        