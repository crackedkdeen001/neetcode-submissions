from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm = defaultdict(int)
        for char in s:
            hm[char] += 1

        for char in t:
            if char not in hm:
                return False
            else:
                hm[char] -= 1

        return all(value == 0 for value in hm.values())
        

    
    """
    we first check if the length of the strings are equal. If not we return false as they can't have the same amount of characters.
    
    if they are the same length, we first initialize a hm mapping of characters → 0 for string s
    we then loop through the second string t, and check if hm[char_t] exists, if it does, we increment the hm[char_t] by 1, if not we return create a new mapping in hm[t] and initialize it to 0
    we then return all(value == 1 for count in values) as if they are anagrams, the counts of hm[char_s] will be initialized to 1 as they will contain the same amount of characters and count 
    """