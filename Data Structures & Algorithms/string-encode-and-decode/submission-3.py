class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""  
        for string in strs:
            encoded += f"{len(string)}~{string}"

        return encoded



    def decode(self, s: str) -> List[str]:
        i = 0
        strings = []
        while i < len(s):
            # get the length of the string
            n = ""
            while s[i] != "~":
                n += s[i]
                i += 1
            
            n = int(n)
            # extract the string from the encoded string
            string = s[i  + 1: i + n + 1]
            strings.append(string)
        
            i += n + 1

        return strings

                


"""
we encode the string such that
lengthDelimiterActualstring

decode works
we traverse the string until we reach the delimiter.
when we reach the delimiter, we stop and take the characters before it as the length of the string
we then truncate the encoded word with the length and add it to a list
repeat

pseudocode
encode()
assume our delimeter is ~
encoded =  "
for string in strs:
    encoded += f"len(string)~string"

return encodedw/<

decode()
i = 0
while :
    n = ""
    while char != "~":
        len  
"""