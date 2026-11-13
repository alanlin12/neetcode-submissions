class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            
            if hours <= h:
                hi = mid - 1
            
            else:
                lo = mid + 1
        
        return lo