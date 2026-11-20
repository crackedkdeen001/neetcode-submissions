class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = 0
        count_s1 = [0] * 26
        for char in s1:
            count_s1[ord(char) - ord("a")] += 1

        for l in count_s1:
            if l != 0:
                need += 1

        for i in range(len(s2)):
            count_sub = [0] * 26
            match = 0
            for j in range(i, len(s2)):
                idx = ord(s2[j]) - ord("a")
                count_sub[idx] += 1
                # avoid irrelevant computations in the case
                # a substring contains more characters than 
                # s1
                if count_s1[idx] < count_sub[idx]:
                    print("index", i, "hi", count_s1[idx], "hello", count_sub)
                    break
                
                if count_s1[idx] == count_sub[idx]:
                    match += 1

                if i == 22 and j == len(s2) - 1:
                    print("index", i, "match", match)
                if match == need:
                    return True

        return False