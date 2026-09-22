class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}

        if len(s) != len(t):
            return False
            
        # count appearance of chars in each string
        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1

        for char in t:
                t_chars[char] = t_chars.get(char, 0) + 1
        
        for key, value in s_chars.items():
            if key in t_chars and value == t_chars.get(key):
                continue
            else:
                return False
            
        return True
            