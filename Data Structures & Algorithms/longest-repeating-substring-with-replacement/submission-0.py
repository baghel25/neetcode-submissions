
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        stack = {}
        res = 0

        for elm in s:
            if elm in stack:
                stack[elm] += 1
            else:
                stack[elm] = 1

            r += 1

            while (r - l) - max(stack.values()) > k:
                stack[s[l]] -= 1
                l += 1

            res = max(res, r - l)

        return res
