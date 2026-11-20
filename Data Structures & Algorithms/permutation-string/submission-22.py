class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count =  {}
        s2_count =  {}

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for c in alphabets:
            s1_count[c] = 0 
            s2_count[c] = 0

        # compute the count of characters in s1 and also 
        # compute the count of characters in the first substring
        # of s2.
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1 
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1 

        matches = 0
        for c in alphabets:
            if s1_count[c] == s2_count[c]:
                matches += 1

        print(matches)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            s2_count[s2[r]] += 1
            # if the count of the character is the same now, increment matches
            if s2_count[s2[r]] == s1_count[s2[r]]:
                matches += 1

            # if the count of the character was the same but now differs,
            # decrement matches
            elif s2_count[s2[r]] == s1_count[s2[r]] + 1:
                matches -= 1 
            
            print(matches)

            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == s1_count[s2[l]]:
                matches += 1
            # if the count of the character was the same but now differs,
            # decrement matches
            elif s2_count[s2[l]] == s1_count[s2[l]] - 1:
                matches -= 1 
            l += 1

        print(matches)
        return matches == 26