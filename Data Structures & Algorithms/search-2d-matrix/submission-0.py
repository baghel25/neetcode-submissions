class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = 0 
        l = 0 
        r = len(matrix) -1

        while l <=r:
            l_rom = 0 
            # print(len(matrix[l]))
            if matrix and 0 <= l < len(matrix) and matrix[l]:
              r_row =len(matrix[l]) -1
            else:
                r_row = -1
            # print("l_rom",l_rom)
            # print("r_row",r_row)
            while l_rom <= r_row:
                m = (l_rom + r_row) // 2
                print(m)
                if matrix[l][m] < target:
                    l_rom = m + 1
                elif matrix[l][m] > target:
                    r_row = m - 1
                else:
                    return True
            l =l+1
            
        return False

            


                


        