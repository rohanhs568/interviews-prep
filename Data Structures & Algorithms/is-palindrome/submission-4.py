class Solution:
    def isPalindrome(self, s: str) -> bool:

        front = 0 
        back = len(s) - 1

        while front < back:
            front_l = s[front]
            back_l = s[back]

            while front < back and not front_l.isalnum():
                front += 1
                front_l = s[front]

            while front < back and not back_l.isalnum():
                back -= 1
                back_l = s[back]

            if front_l.lower() != back_l.lower():
                return False

            front += 1
            back -= 1

        return True

