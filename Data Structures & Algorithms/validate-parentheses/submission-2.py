class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for i in range(len(s)):
            # openings
            if s[i] in brackets.values():
                stack.append(s[i])
                continue
            
            if not stack:
                return False

            # closings
            if stack.pop() != brackets.get(s[i]):
                return False

        return not stack 

