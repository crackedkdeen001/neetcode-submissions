class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hm = {}

        for i in range(n):
            s = "".join(sorted(strs[i]))
            if s in hm:
                hm[s].append(strs[i])
            else:
                hm[s] = []
                hm[s].append(strs[i])

        grp_anagrams = []
        for _, anagrams in hm.items():
            grp_anagrams.append(anagrams)

        return grp_anagrams







    """  
       brute force
       we initialize an empty list for our group anagrams
       use a double for loop to check if a sorted string is equal to other sorted strings in front of it in the array
       we initialize an empty anagram list in the outer for loop containing the string we want to check other strings against
       we then sort the current string and save it in a variable
       in the inner for loop, we then sort the other string we are comparing the string in the outer loop to 
       if they are the same, add the unsorted string in the inner for loop to the anagram array declared in the outer for loop 
       
       at the end of the outer "for" loop, append the anagram array to the group anagrams 
    
    === HANDLING DUPLICATES ===
    when we have seen a string that is index > i that forms a anagram with the string at index i, we set it to a special character, since the strings will only comprise of english lowercase letters.
    And also in the outer loop, if we encounter said special character, we skip the iteration, as an anangram has already been found for that particular character

     OPTIMAL    
     we create a hashmap which is going to contain the sorted string as the key and an empty list as the value
     if a string's anagram doesn't exist yet in the hashmap, we create a key of the sorted anagram and a list containing the unsorted string
     if it does, we just append it to the list

    """
