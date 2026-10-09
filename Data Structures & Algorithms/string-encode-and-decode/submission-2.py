class Solution:

    def encode(self, strs: List[str]) -> str:

        print("list",strs)
        encode = ""
        for num in strs:
            lent = str(len(num))
            string = lent+"#"+num
            encode += string
        return encode




    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            end = s.index("#", index)
            str_len = int(s[index:end])

            start_index = end + 1
            string = s[start_index:start_index + str_len]
            result.append(string)

            index = start_index + str_len

        return result





