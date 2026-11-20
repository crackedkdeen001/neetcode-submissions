class Solution:
    def trap(self, height: List[int]) -> int:
        # bars with length 1 or 2 can't trap water
        if len(height) in [1, 2]:
            return 0 

        # total = 0
        # l = 0
        # r = 1
        # # water can only be trapped if the next bars are shorter in height
        # # than the bar at s[l] and there exists a bar t at index >= l + 2
        # # such that, bar t >= s[l] in height
        # # so we a left and right pointer, left 
        # while r < len(height):
        #     water = 0 
        #     while r < len(height) - 1 and height[l] > height[r]:
        #         water += height[l] - height[r]
        #         r += 1

            
        #     if r < len(height) - 1 and height[r] >= height[l]:
        #         total += water
            
        #     # move our l and r as we've checked for all trapped water between l and r
        #     l = r
        #     r = r + 1

        # return total

        total = 0
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        l_max = 0
        r_max = 0

        for l in range(n):
            prefix_max[l] = l_max
            l_max = max(l_max, height[l])
        
        for r in range(n - 1, -1, -1):
            suffix_max[r] = r_max
            r_max = max(r_max, height[r])

        for i in range(n):
            water = min(suffix_max[i], prefix_max[i]) - height[i]
            
            if water > 0:
                total += water

        return total