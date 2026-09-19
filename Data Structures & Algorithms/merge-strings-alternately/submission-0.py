class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        ptr_a = 0
        ptr_b = 0

        while ptr_a < len(word1) and ptr_b < len(word2):
            curr_str = word1[ptr_a] + word2[ptr_b]
            res += curr_str
            ptr_a += 1
            ptr_b += 1

        if ptr_b < len(word2):
            res += word2[ptr_b:]

        if ptr_a < len(word1):
            res += word1[ptr_a:]

        return res