class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        unique_a = set()

        for i, num in enumerate(nums):
            if num in unique_a:
                continue
            unique_a.add(num)

            stat = i + 1
            end = len(nums) - 1
            target = -num

            while stat < end:
                elm_sum = nums[stat] + nums[end]

                if elm_sum < target:
                    stat += 1
                elif elm_sum > target:
                    end -= 1
                else:
                    res.append([num, nums[stat], nums[end]])
                    stat += 1
                    end -= 1

                    while stat < end and nums[stat] == nums[stat - 1]:
                        stat += 1

        return res