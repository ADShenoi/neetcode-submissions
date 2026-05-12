class Solution:
    def check_arr(self, arr:List[str]) -> bool:
        bucket = [0] * 10
        for i in arr:
            if i != '.':
                bucket[int(i)] += 1
                if bucket[int(i)] > 1:
                    return False
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_arr(row):
                return False

        for col in zip(*board):
            if not self.check_arr(col):
                return False
                
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[r+i][c+j])
                if not self.check_arr(box):
                    return False 
        
        return True
        