class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) -1
        l = 0    
        m = 0   
        while l <= r:
            m = (r + l) // 2 
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                print(l , r)
                return m

        return -1


        