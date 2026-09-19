# arr = [2,4,5,8] k = 2 x = 6
#        ^     ^
#        L     R
# |6 - 2| = 4. ok then given the array is sorted, if we move right, we know the ABSOLUTE difference will likely get smaller, so we move the right ptr


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        l = 0
        r = len(arr) - 1

        while (r-l) > k-1:            
            if abs(x - arr[l]) < abs(x - arr[r]):
                r -= 1
            elif abs(x - arr[l]) == abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        
        return arr[l:r+1]

        