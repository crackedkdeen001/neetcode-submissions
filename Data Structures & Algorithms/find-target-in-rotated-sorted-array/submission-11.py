class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while r >= l:
            mid = (l + r) // 2

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid 

        print(mid)

        def binary_search(arr: list[int], left: int, right: int):
            while right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left_side = binary_search(nums, 0, mid - 1)
        if left_side != -1:
            return left_side

        return binary_search(nums, mid, len(nums) - 1)