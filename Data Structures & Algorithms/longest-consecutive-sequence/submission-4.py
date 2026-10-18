class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        seen_values = set(nums)
        ans = 0

        for num in seen_values:
            if num - 1 not in seen_values: 
                curr = 1
                while num + curr in seen_values:
                    curr += 1
                ans = max(curr, ans)
        
        return ans