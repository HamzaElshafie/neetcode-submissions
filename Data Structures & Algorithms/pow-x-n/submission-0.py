class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = helper(x, abs(n))

        return res if n > 0 else 1 / res
        
        
def helper(x, n):
    if n == 0:
        return 1
    
    if x == 0:
        return 0

    half_power = helper(x, n // 2)
    full_power = half_power * half_power
    
    return full_power if n % 2 == 0 else x * (full_power)