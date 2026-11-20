class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
                # while j >= i:
        #     if nums[i] == val and nums[j] != val:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     elif nums[i] == val and nums[j] == val:
        #         j -= 1
        #         continue
            
        #     i += 1
        # count = nums.count(val)
        # new_length = len(nums) - count

        
        l = 0
        r = len(nums)

        while l < r:
            if nums[l] == val:
                nums[l], nums[r - 1] = nums[r - 1], nums[l]
                r -= 1
            else:
                l += 1

        return l      