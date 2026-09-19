class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(idx, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for char in keypad[digits[idx]]:
                backtrack(idx+1, curr_str + char)

        backtrack(0, "")
        return [] if digits == "" else res
