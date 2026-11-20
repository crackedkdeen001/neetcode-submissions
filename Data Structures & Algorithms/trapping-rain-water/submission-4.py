class Solution:
    def trap(self, height: List[int]) -> int:
        # bars with length 1 or 2 can't trap water
        if len(height) in [1, 2]:
            return 0 

        def can_water_be_trapped(height1, height2):
            return True if height1 - height2 >= 0 else False
            
        water = 0
        l = 0
        r = len(height) - 1
        max_l, max_r = height[0], height[-1]
        # water can only be trapped if the next bars are shorter in height
        # than the bar at s[l] and there exists a bar t at index >= l + 2
        # such that, bar t >= s[l] in height
        # so we a left and right pointer, left 
        while r > l :
            if max_l < max_r:
                l += 1
                if can_water_be_trapped(max_l, height[l]):
                    water += max_l - height[l]
                max_l = max(max_l, height[l])
            else:
                r -= 1
                if can_water_be_trapped(max_r, height[r]):
                    water += max_r - height[r]
                max_r = max(max_r, height[r])
        return water

        # precompute the max bar to the left and right for each element before hand
        # and then reference it in calculation
        # NOTE: repeated work == store
        # water = 0
        # n = len(height)
        # prefix_max = [0] * n
        # suffix_max = [0] * n
        # l_max = 0
        # r_max = 0

        # for l in range(n):
        #     prefix_max[l] = l_max
        #     l_max = max(l_max, height[l])
        
        # for r in range(n - 1, -1, -1):
        #     suffix_max[r] = r_max
        #     r_max = max(r_max, height[r])

        # for i in range(n):
        #     water = min(suffix_max[i], prefix_max[i]) - height[i]
            
        #     if water > 0:
        #         water += water

        # return water