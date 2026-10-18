class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_values = {}
        for num in nums:
            if num in seen_values: return True
            else:
                seen_values[num] = 1

        return False