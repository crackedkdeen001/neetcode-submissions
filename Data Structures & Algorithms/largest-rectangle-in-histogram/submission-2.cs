public class Solution {
    public int LargestRectangleArea(int[] heights) {
        int maxArea = 0;
        for (int i = 0; i < heights.Length; i ++){
            int height = heights[i];

            int l_width = 0;
            int r_width = 0;

            int l = i - 1;
            int r = i + 1;

            while (l > -1)
            {
                if (heights[l] < height)
                {
                    break;
                }
                else
                {
                    l_width++;
                }
                l--;
            }

            while (r < heights.Length) 
            {
                if (heights[r] < height)
                {
                    break;
                }
                else
                {
                    r_width++;
                }
                r++;
            }

            int width = 1 + l_width + r_width;
            maxArea = Math.Max(maxArea, height * width);
        }

        return maxArea;
    }
}
