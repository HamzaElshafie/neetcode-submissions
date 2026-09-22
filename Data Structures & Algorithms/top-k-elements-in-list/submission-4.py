class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurances of ints in nums
        counts = {}
        for val in nums:
            counts[val] = 1 + counts.get(val, 0)

        # collect occurances into buckets {freqs, list[int]}
        freqs_buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in counts.items():
            freqs_buckets[value].append(key)

        res = []

        for frequency in range(len(freqs_buckets)-1, -1, -1):
            for number in freqs_buckets[frequency]:
                res.append(number)

            if len(res) == k:
                return res