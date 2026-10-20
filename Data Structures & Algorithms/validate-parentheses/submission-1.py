class Solution:
    def isValid(self, s: str) -> bool:
        valid_sequences = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in valid_sequences:
                if len(stack) > 0:
                    if valid_sequences[ch] != stack.pop(): return False
                else:
                    stack.append(ch)
            else: stack.append(ch)
        
        return (len(stack) == 0)