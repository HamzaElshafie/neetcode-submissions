class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            freqs_map = {}
            max_freq = 0
            for j in range(i, len(s)):
                freqs_map[s[j]] = 1 + freqs_map.get(s[j], 0)
                max_freq = max(max_freq,  freqs_map[s[j]])
                window_size = j - i + 1
                if (window_size - max_freq) <= k:
                    res = max(res, window_size)

        return res