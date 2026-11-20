from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = l = 0
        most_freq = None
        
        for r in range(len(s)):
            count[s[r]] += 1
            if most_freq is None or count[s[r]] > count[most_freq]:
                most_freq = s[r]

            while (r - l + 1) - count[most_freq] > k:
                count[s[l]] -= 1 
                l += 1

                if count[s[l]] > count[most_freq]:
                    most_freq = s[l]

                if count[s[r]] > count[most_freq]:
                    most_freq = s[r] 
               
            res = max(res, r - l + 1)
            
        return res
