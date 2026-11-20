import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = float("-inf")
        
        while r >= l:
            res = 0
            mid = (r + l) // 2
            for bananas in piles:
                res += math.ceil(bananas / mid)
            
            if res > h:
                l = mid + 1
            else: 
                k = mid
                r = mid - 1
        return k