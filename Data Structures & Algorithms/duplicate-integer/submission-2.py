class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempDis = set()
        for elm in nums:
            # print("elm",elm)
            if elm in tempDis:
              return True 
            tempDis.add(elm)
            
        return False

        
        