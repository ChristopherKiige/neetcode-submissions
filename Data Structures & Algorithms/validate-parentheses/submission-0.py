class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
            
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:  # It's a closing bracket
                # If stack is empty or top doesn't match the opener, it's invalid
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:              # It's an opening bracket
                stack.append(char)
                
        # Valid only if all opening brackets were closed (stack is empty)
        return len(stack) == 0