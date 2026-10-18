class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for num in nums:
            vals[num] = 1 + vals.get(num, 0)
        
        return(sorted(vals, key=vals.get, reverse=True))[:k]