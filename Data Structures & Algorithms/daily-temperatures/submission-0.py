class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)
        res = [0]*temp_len
        stack = [] # [index,val]

        for idx ,val in enumerate(temperatures):

            while stack and val > stack[-1][1]:
                index, last_val = stack.pop()
                res[index] = idx - index
               
            stack.append([idx,val])
        return res


