class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstInput = {}
        
        if len(s) != len(t):
            return False

        for elm in s:
            val = 1
            if elm in firstInput:
                val += firstInput[elm]

            firstInput[elm] = val
            
        for elm in t:
            if elm not in firstInput:
                return False

            firstInput[elm] -= 1

            if firstInput[elm] == 0:
                del firstInput[elm]
        return not firstInput 
