class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # if a and the previous number are the same, they are duplicates hence skip
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                threesum = a + nums[j] + nums[k]

                if threesum > 0:
                    k -= 1
                elif threesum < 0:
                    j += 1
                else:
                    triplets.append([a, nums[j], nums[k]])
                    k -= 1
                    while nums[k + 1] == nums[k] and k > j:
                        k -= 1
        return triplets
