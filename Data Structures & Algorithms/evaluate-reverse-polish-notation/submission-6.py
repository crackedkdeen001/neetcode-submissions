class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["/", "+", "*", "-"]
        stack = []

        for token in tokens:
            if token in op:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "/":
                    result = eval(f"{operand1} / {operand2}")
                    result = int(result)
                else:
                    result = eval(f"{operand1} {token} {operand2}")
                stack.append(result)
            else:
                stack.append(token)

        return int(stack.pop())












        
        """
        container = operators
        stack = []
        for each element in tokens:
            if element is in op:
                operand2 = stack.pop()
                operand1 = stack.pop()

                result = eval("{operand1} {op} {operand2}")
                add the result to the stack so it can be used for calculations
            else:
                stack.append(element)

        return stack.pop()
        """