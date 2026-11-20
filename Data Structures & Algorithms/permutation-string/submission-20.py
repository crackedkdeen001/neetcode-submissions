class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = {}
        for char in s1:
            count_s1[char] = 1 + count_s1.get(char, 0)

        need = len(count_s1)
        for i in range(len(s2)):
            count_sub = {}
            match = 0
            for j in range(i, len(s2)):
                count_sub[s2[j]] = 1 + count_sub.get(s2[j], 0) 
                # avoid irrelevant computations in the case
                # a substring contains more characters than 
                # s1
                if count_s1.get(s2[j], 0) < count_sub[s2[j]]:
                    break
                
                if count_s1.get(s2[j], 0) ==  count_sub[s2[j]]:
                    match += 1

                if match == need:
                    return True

        return False