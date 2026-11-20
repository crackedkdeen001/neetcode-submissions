class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hm = {}
       for i in range(len(nums)):
            value = target - nums[i]
            if value in hm:
                return [hm[value], i]

            hm[nums[i]] = i
            