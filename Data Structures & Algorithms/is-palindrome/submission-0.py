class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = "".join(c.lower() for c in s if c.isalnum())
        
        l, r = 0, len(palindrome) - 1
        while l <= r:
            if palindrome[l] != palindrome[r]: return False
            l += 1
            r -= 1

        return True