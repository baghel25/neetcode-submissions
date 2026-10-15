class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        stat = 0 
        end = length-1
        for index ,elm in enumerate(numbers):
            sumelm = numbers[stat] + numbers[end]
            if sumelm > target:
                end -=1
            elif sumelm < target:
                stat += 1
            else:
                # print(numbers[stat] , numbers[end])
                return [stat+1,end+1]

           


        