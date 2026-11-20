class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mini = float("+inf")

        while l <= r:
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                break
            
            mid = (l + r) // 2
            mini = min(mini, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
            
        return mini