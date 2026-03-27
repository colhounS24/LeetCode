class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operands = set(["+", "-", "*", "/"]) # Use a set for better look-up complexity

        for token in tokens:
            # Case where it is an operand
            if token in operands:
                # could use switch statements, not too much of a difference here tbh
                b = stack.pop()
                a = stack.pop() 
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack.pop()
