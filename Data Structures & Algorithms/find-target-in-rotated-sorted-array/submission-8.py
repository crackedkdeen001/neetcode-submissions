class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # find the pivot
        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(arr: list[int], left: int, right: int):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return -1 
        
        # compute the result for the first sorted half
        res = binary_search(nums, 0, pivot - 1)
        if res != -1:
            return res

        # if it's not on the left...
        # it's on the right
        return binary_search(nums, pivot, len(nums) - 1)