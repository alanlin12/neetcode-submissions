class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        mid = 0
        while lo <= hi:
            mid = (lo + hi) // 2
        
            if nums[mid] > nums[hi]: lo = mid + 1

            elif nums[mid] < nums[hi]: hi = mid

            else: return nums[lo]
        
        return nums[lo]

        