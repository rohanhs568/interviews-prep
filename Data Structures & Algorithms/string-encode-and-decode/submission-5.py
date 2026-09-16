class Solution:

    # using #n method

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s: str) -> List[str]:

        #  5#Hello5#World, len 14

        decoded = []

        i = 0
        

        while i < len(s):
            curr_length = ""

            while s[i] != "#":
                curr_length += str(s[i])
                i += 1

            decoded.append(s[i+1:(i+1+int(curr_length))])
            i+=int(curr_length)+1
    
        return decoded

            

        


