class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        count_s1 = [0] * 26

        for char in s1:
            count_s1[ord(char) - ord("a")] += 1

        for i in range(len(s1), len(s2) + 1):
            count_sub = [0] * 26
            for j in range(l, i):
                count_sub[ord(s2[j]) - ord("a")] += 1
            
            if count_sub == count_s1:
                return True
            else:
                pass
            
            l += 1

        return False