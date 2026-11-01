class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) -1

        while l <=r:
            m = (l+r)//2
            # print("m",m,nums[m])
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            res = min(res,nums[m])

            # print(nums[m] > nums[l],nums[m] ,nums[l],nums[r])
            if nums[m] >=nums[l]:
                l = m + 1
                

            else:
                r = m -1
            # print("res",res)

        return res

            
            

        