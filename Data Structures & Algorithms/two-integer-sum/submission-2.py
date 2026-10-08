class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sub = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in dict_sub:
                return [dict_sub[rem], i]

            dict_sub[nums[i]] = i
