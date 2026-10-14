class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = 9

        # Check rows
        for i in range(board_len):
            dup_chek = set()
            for j in range(board_len):
                item = board[i][j]
                if item.isdigit():
                    if item in dup_chek:
                        return False
                    dup_chek.add(item)

        # Check columns
        for i in range(board_len):
            dup_chek = set()
            for j in range(board_len):
                item = board[j][i]
                if item.isdigit():
                    if item in dup_chek:
                        return False
                    dup_chek.add(item)

        # Check 3×3 boxes
        for blc in range(board_len):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (blc // 3) * 3 + i
                    col = (blc % 3) * 3 + j
                    irm = board[row][col]

                    if irm.isdigit():
                        if irm in seen:
                            return False
                        seen.add(irm)

        return True