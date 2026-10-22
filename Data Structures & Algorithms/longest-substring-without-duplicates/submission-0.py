
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr = set()
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in curr:
                curr.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                curr.remove(s[i])
                i += 1

        return max_len
