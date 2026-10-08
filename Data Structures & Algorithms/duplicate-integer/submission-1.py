class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempDis = []
        for elm in nums:
            # print("elm",elm)
            if elm in tempDis:
              return True 
            tempDis.append(elm)
            
        return False

        
        