class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        ptr_a = 0
        ptr_b = 0

        while ptr_a < len(word1) and ptr_b < len(word2):
            res.append(word1[ptr_a])
            res.append(word2[ptr_b])
            ptr_a += 1
            ptr_b += 1
        
        res.extend(word1[ptr_a:])
        res.extend(word2[ptr_b:])

        return "".join(res)