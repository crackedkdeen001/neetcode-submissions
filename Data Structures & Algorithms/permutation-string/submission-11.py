class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        count_s1 = [0] * 26

        for char in s1:
            count_s1[ord(char) - ord("a")] += 1
        cp_count_s1 = count_s1[:]

        for i in range(len(s1), len(s2) + 1):
            for j in range(l, i):
                count_s1[ord(s2[j]) - ord("a")] -= 1

            includes = all(count == 0 for count in  count_s1)
            print(count_s1)
            if includes:
                return True
            else:
                pass
            
            l += 1
            count_s1 = cp_count_s1[:]

        return False