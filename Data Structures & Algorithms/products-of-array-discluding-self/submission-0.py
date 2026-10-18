class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, postfix = 1, 1
        for pre in range(len(nums)):
            res[pre] = prefix
            prefix *= nums[pre]
        
        for post in range(len(nums) - 1, -1, -1):
            res[post] *= postfix
            postfix *= nums[post]
    
        return res
      