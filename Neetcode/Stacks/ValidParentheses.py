class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0 or len(s) == 0:
            return False
        
        closing_symbols = ["]","}",")"]
        stack = []

        p_map = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for char in s[:]:
            if char in closing_symbols and len(stack) >0:
                if stack.pop() == p_map[char]:
                    continue

                return False
            stack.append(char)

        return len(stack) == 0
        
