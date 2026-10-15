class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cab = 0
        min_height = 1 
        start = 0 
        end = len(heights) - 1  
        width = 1 

        while start < end :
            start_val = heights[start]
            end_val = heights[end]
            width = end - start
            min_height = min(start_val,end_val)
            max_cab = max(max_cab,width*min_height)
            if start_val < end_val:
                start +=1
            else:
                end -= 1

        return max_cab




        # idex = end - start should > max 

        