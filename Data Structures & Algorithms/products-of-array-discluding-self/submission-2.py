class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        # initialize prefix and suffix array
        prefix = [1] * n
        suffix = [1] * n

        # start at index 1 as no element exists before index 0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # start at index len(nums) - 2 as no index exists after index len(n - 1)
        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        # compute the output
        for i in range(n):
            output.append(prefix[i] * suffix[i])

        return output
        



    """
    previous brute force method was a double for loop


    I used hints, keep that in mind
    I used the prefix, suffix technique. Where instead of using a double for loop 
    that computes all possible products except the element at index i.
    I commputed the prefix multplication of the array, which is product of all elements before the element at index i non inclusive, while suffix is the product of elements after it except the element at index i

    to get the output at index i, we then multiply prefix[i] with suffix[i] to get the
    output

    """ 