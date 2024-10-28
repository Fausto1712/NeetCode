from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"/","+","-","*"}:
                b = stack.pop()
                a = stack.pop()
                if token == "/":
                    stack.append(int(a / b))
                elif token == "-":
                    stack.append(a - b)
                elif token == "+":
                    stack.append(a + b)
                elif token == "*":
                    stack.append(a * b)
            else:
                stack.append(int(token))

        return stack[0]
    
tokens = ["4","13","5","/","+"]

print()
print(f"Result: {Solution.evalRPN(Solution, tokens)}")
print()