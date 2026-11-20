from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(t) > len(s):
        #     return ""
        if t == "":
            return ""

        t_count = defaultdict(int)
        window = defaultdict(int)
        have = 0
        need = 0
        l = 0
        res = [-1, -1]
        len_res = float("inf")

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
            if t_count.get(c) == 1:
                need += 1
            
        # or
        # have = len(t_count)
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1
            
            # we want to move our left pointer until 
            # have and need aren't the same
            while have == need:
                # update our result if we find
                # a smaller substring
                if (r - l + 1) < len_res:
                    res[0], res[1] = l, r
                    len_res = r - l + 1

                # remove our left character from the window
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1
        
        l, r = res
        return s[l : r + 1]
