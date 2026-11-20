class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # length of string  + delimiter + actual string 

        for s in strs:
            res += str(len(s)) + "!" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                # get the index of '!' so we know the length is just before it
                j += 1

            # turns the length to an integer
            string_len = int(s[i : j])

            # gets the actual string s
            string = s[j + 1 : j + string_len + 1]
            res.append(string)

            i = j + string_len + 1

        return res
            
        