class Solution:
    def isPalindrome(self, s: str) -> bool:
        elm = "".join(s.lower())
        strt = ""
        for index, char in enumerate(elm):
            if char.isalnum():
                strt += char

        rev = strt[::-1]
        return strt == rev




        