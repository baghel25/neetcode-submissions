class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in bucket:
                logest = 1
                current = num 
                while current+1 in bucket:
                    current +=1 
                    logest +=1
            
                res = max(logest,res)

        return res

            



        


