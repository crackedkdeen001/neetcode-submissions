public class Solution {
    public int FindMin(int[] nums) {
        int l = 0;
        int r = nums.Length - 1;
        int res = nums[0];

        while (r >= l){
            if (nums[r] > nums[l]){
                res = Math.Min(res, nums[l]);
                break;
            }

            double idk = (r + l) / 2;
            int m = (int) Math.Floor(idk);
            res = Math.Min(res, nums[m]);

            if (nums[m] >= nums[l]){
                l = m + 1;
            }
            else{
                r = m - 1;
            }
        }

        return res;
    }
}
