class Solution:

    def encode(self, strs: List[str]) -> str:
        # idea : 
        # dots indicate gaps, colon indicates start of string
        # have a indices of all the first letters of the words:
        # ["cart", "patch", "shapes", "it"]
        # eg: 0.4.9.14:cartpatchshapesit

        if not strs:
            return ""

        encoded = ""

        total = 0

        for string in strs:
            encoded += ("." + str(total))
            total += len(string)
        
        encoded += ":" 
        
        for string in strs:
            encoded += string

        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        # build positions array

        positions = []
        string = ""

        num = ""
        for i, char in enumerate(s[1:]):           

            if char == ":":
                positions.append(int(num))
                remaining_string = s[i+2:]
                break

            elif char == ".":
                positions.append(int(num))
                num = ""

            else:
                num += char

        decoded = []

        # ["cart", "patch", "shapes", "it"]
        # eg: 0.4.9.14:cartpatchshapesit
        # positions = [0, 4, 9, 14]

        for i, position in enumerate(positions[:-1]):
            curr = remaining_string[position:positions[i+1]]
            decoded.append(curr)

        decoded.append(remaining_string[positions[-1]:])
    
        return decoded

            
