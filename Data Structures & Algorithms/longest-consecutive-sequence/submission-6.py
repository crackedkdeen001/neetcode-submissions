class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for n in nums:
            count = 1
            if n - 1 in elements:
                continue
            
            after = n + 1
            while after in elements:
                count += 1
                after += 1

            longest = max(count, longest)

        return longest

