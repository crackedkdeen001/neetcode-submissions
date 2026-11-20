class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                j = stack[-1][0] 
                result[j] = i - j
                stack.pop()
            
            stack.append((i, temperature))
        
        return result