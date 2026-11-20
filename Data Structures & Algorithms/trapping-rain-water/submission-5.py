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
        max_l, max_r = height[l], height[r]
        # how water can be trapped is dependent on the max to the left of the bt
        # and to the right of the bar.
        # Now, the amount of water that can be trapped is dependent on the 
        # smaller of the two bars at left and right because the bigger one will
        # be bottlenecked by it.
        # what we're doing here is that we have the max of the left and right
        # seen so far and if the max at the left is smaller than one on the right,
        # we move our left pointer forward and calculate the water at that point
        # by just doing the max_l - height[r] cuz the right bar that is bigger 
        # is bottlenecked by the left so we use the left for our calculation of 
        # the water.
        # we do same for right with the right pointer and always update our r_max
        # and l_max after the computations.
        while r > l :
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                if can_water_be_trapped(max_l, height[l]):
                    water += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                if can_water_be_trapped(max_r, height[r]):
                    water += max_r - height[r]
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