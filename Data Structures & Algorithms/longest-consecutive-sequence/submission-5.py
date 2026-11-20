class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) 
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr = num
                consec = 0 
                while curr in nums:
                    consec += 1
                    curr += 1
                
                longest = max(longest, consec)

        return longest

    """
    Brute force 
    sort the array then count the number of consecutive elements
    
    input
    an array of integers

    output
    the number of consecutive numbers in the array

    edge cases
    the array is empty
    the array is not empty but there are no consecutive elements

    solution above, 
    we convert our element to a set to remove duplicate values from the original array
    
    """ 