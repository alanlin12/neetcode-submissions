class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() 

        for anchor in range(len(nums) - 2):
            if anchor > 0 and nums[anchor] == nums[anchor-1]: continue
            compliment_values = {}
            for scan in range(anchor + 1, len(nums)):
                compliment = -(nums[anchor] + nums[scan])
                if compliment in compliment_values:         
                    ans.append([nums[anchor], nums[scan], compliment])
                compliment_values[nums[scan]] = nums[scan]
                    

        return list(set(tuple(r) for r in ans))