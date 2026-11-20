from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        char_count =  [0] * 26
        for char in s1:
            char_count[ord(char) - ord("a")] += 1

        char_count2 = char_count[:]
        # this is a fixed window problem with len(s1) as the size of the fixed window
        for r in range(len(s1), len(s2) + 1):
            sub_s = s2[l : r]
            for char in sub_s:
                char_count2[ord(char) - ord("a")] -= 1

            # the any function returns true if any character is truthy in an iterable
            # and we're expecing all values to be falsy in the count
            # since a permutation should have the same number of characters
            contains = all(n == 0 for n in char_count2)
            print(char_count2)
            if contains:
                return True
            else:
                pass
            
            l += 1
            char_count2 = char_count[:]

        return False
    