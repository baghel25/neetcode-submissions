
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dic = {}
        sub_set = {}
        srt_len = len(s1)
        l = 0

        if srt_len > len(s2):
            return False

        for ch in s1:
            s1_dic[ch] = s1_dic.get(ch, 0) + 1

        for r in range(len(s2)):
            sub_str = s2[r]
            sub_set[sub_str] = sub_set.get(sub_str, 0) + 1

            if r - l + 1 > srt_len:
                left_char = s2[l]
                sub_set[left_char] -= 1

                if sub_set[left_char] == 0:
                    del sub_set[left_char]

                l += 1

            if sub_set == s1_dic:
                return True

        return False
