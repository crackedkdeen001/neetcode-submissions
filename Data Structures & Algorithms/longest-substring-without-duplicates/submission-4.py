class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # remove the characters up until the duplicate characte
            while s[r] in charset:
                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            # r - l = window size, + 1 as a padding
            res = max(res, r - l + 1)


        return res