class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} 

        for elm in strs:
            arr_0 = [0] * 26
            for char in elm:
                index = ord(char) - ord("a")
                arr_0[index] += 1 

            key = tuple(arr_0)
            if key not in dic:
                dic[key] = []

            dic[key].append(elm)

        return list(dic.values())