class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math

        prod_arr = []
        for i, _ in enumerate(nums):
            mult = math.prod(nums[i + 1:]) * math.prod(nums[:i])
            prod_arr.append(mult)

        return prod_arr
        