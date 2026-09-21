class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest



# s = "zxyzxyz"

# This one i think is straightforward. We start l and r at 0 and keep going hmm but wait so i was thinking for eg we can start at `z` and then expand to `x`, they are not same so expand again to include `y`, but then if we only compare z != y this will be true but that doesn't mean that whats at the position of x is not same as what at the position of y. Do u understand? ughhh idk why am i so stupid today