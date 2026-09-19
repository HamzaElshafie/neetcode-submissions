# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Approach:
# our search space is [1, 2, 3, 4, ....., n]
# we can do binary search guessing the mid (l + r) // 2
# call guess(mid)
# if guess is equal (0) we return
# if guess is higher (-1), search left region
# if guess is lower (1), search right region

# [1, 2, 3, 4, 5, 6]

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while True:
            m = (l + r) // 2

            match guess(m):
                case 0:
                    return m
                case -1:
                    r = m - 1
                case 1:
                    l = m + 1

