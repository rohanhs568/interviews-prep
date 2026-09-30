class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        
        opp_dict = {
            "(": ")",
            "[": "]",
            "{": "}",    
        }

        opens = set(opp_dict.keys())
        close = set(opp_dict.values())

        stack = []

        for char in s:
            if char in opens:
                stack.append(char)

            if char in close:
                if not stack:
                    return False

                if char == opp_dict[stack[-1]]:
                    stack.pop()

                else:
                    return False

        if not stack:
            return True

        else:
            return False


        