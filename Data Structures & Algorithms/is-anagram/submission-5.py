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
        

    
    # we first check if the length of the strings are equal. If not, we return false 
    # as they can't have the same amount of characters.
    # if they are the same length, we first create
    # a hm mapping of characters to their 
    # count in the string *s* using a for loop.
    # we then loop through the second string t, and check if the current char
    # exists in the hm. If it does, we decrement the count of the character by 1
    # and if it doesn't, we return False
    # We then check if all the values within the hm are zero because
    # anagrams have the same number of characters, so the count for all
    # characters should be zero
    