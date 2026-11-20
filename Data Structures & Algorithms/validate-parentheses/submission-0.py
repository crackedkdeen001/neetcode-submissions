class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []

        for char in s:
            if char in mapping.keys():
                stack.append(char)  
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if mapping[top] == char:
                    continue 
                else:
                    return False

        return len(stack) == 0