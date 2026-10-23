class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        values = {}

        for r in range(len(s)):
            values[s[r]] = 1 + values.get(s[r], 0)
            while(r - l + 1) - max(values.values()) > k:
                values[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res