class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                op2 = stack.pop()
                op1 = stack.pop()
                
                if token == "+":
                    stack.append(int(op1) + int(op2))
                elif token == "-":
                    stack.append(int(op1) - int(op2))
                elif token == "*":
                    stack.append(int(op1) * int(op2))
                elif token == "/":
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return int(stack[0])