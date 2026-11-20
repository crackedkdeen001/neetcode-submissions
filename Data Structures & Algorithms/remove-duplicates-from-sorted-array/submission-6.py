class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = nums[:]  
        nums_dup = {}
        
        for i in range(len(nums2)):
            if nums2[i] in nums_dup:
                nums.remove(nums2[i])

            nums_dup[nums2[i]] = i

        return len(nums)