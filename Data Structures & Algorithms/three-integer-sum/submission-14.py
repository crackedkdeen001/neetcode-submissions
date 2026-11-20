from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            # handle duplicates values
            if i - 1 >= 0  and nums[i - 1] == nums[i]:
                continue

            num1  = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                threesum = num1 + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # checks for duplicates among the numbers i + 1 to n - 1
                    while nums[l - 1] == nums[l] and r > l:
                        l += 1
        
        return res
        

        # for i in ra                nge(n):
        #     if i - 1 > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))

        # res = list(res)
        # for i in range(len(res)):
        #     res[i] = list(res[i])



        """
        bruteforce
        we're gonna have 3 nested for loops that start from the first index
        and try to find a possible triplet that adds up to 0.

        we are going to use a triplets when they have been
        found and add it to a list
        but it's still possible for duplicates triplets to arise so we sort
        the array at first.

        at the beginning of the outermost loop, we check whether the current 
        number is the same as the previous number. If so, we skip that
        iteration to avoid wasteful calculation

        at the end of the triple loop, we convert the triplets tuples into a 
        list and return the outer loop

        psuedocode    
        nums.sort()
        res = []
        for i in 1 to nums.Len
            if i - 1 < 1 and nums[i] == nums[i -1]:
                continue
            for j in i + 1 to num.len
                for k in j + 1 to num.len
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        
        return res
        algorithm above is flawed, doesn't account for when all the numbers 
        are 0s. That's what the set and tuples were for


        """

