class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            height = heights[i]
            left_w = right_w = 0 

            l = i - 1
            r = i + 1
        
            while l > -1:
                if heights[l] < height:
                    break
                else:
                    left_w += 1  
                l -= 1

            while r < len(heights):
                if heights[r] < height:
                    break
                else:
                    right_w += 1
                r += 1

            width = 1 + right_w + left_w
            max_area = max(max_area, height * width)

        return max_area



        """
        what do we need?
        height of a rectangle  
        width of a rectangle

        we can set the width of the rectangle to be equal to one.
        if the previous bar is greater or equal to the current bar, we increase
        the width of the rectangle by 1
        else we reset the current width to 1

        bruteforce
        two pointer approach
        we select a bar the array 
        left and right pointer for gettting the max posssible width = 0
        left one checks for the greatest width found to the left of the array
        right one checks for the greatest width found to the right of the array
        left_w and right_w = 0

        max_area = 0

        while l > -1:
            if heights[l] == 0 or heights[l] < curr_height:
                break
            else: 
                left_w += 1
            left -= 1
        
        while r < len(heights) - 1:
            brekak
            if height[r] == 0 or heights[r] < curr_height:
                break
            else:
                right_w += 1
            
            right += 1

        width = left_w + right_w
        max_area = max(max_area, height * width)

        return max_area

        rather than getting the max of the left and right width, we increment   the width for every bar that is >= the height and if we see a bar that is less than the current height, we break and take the current width as the biggest possible width
        """

       
        