class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        array = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count:
            index = count[num]
            array[index].append(num)

        result = []
        for index in range(len(nums), 0, -1):
            for num in array[index]:
                result.append(num)
                if len(result) == k:
                    return result