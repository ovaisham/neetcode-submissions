class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valSet = set([str(i) for i in range(1,10)])
        board_columns = [[] for i in range(len(board))]
        board_sub_boxes = [[] for i in range(len(board))]

        isValid = True
        for i in range(len(board)):
            for j in range(len(board)):
                board_columns[j].append(board[i][j])
                board_sub_boxes[((i//3)*3) + (j//3)].append(board[i][j])

        for item in board:
            if self.isValList(item) != True:
                return False
        for item in board_columns:
            if self.isValList(item) != True:
                return False
        for item in board_sub_boxes:
            if self.isValList(item) != True:
                return False
        return True


    def isValList(self, valList: List[str]) -> bool:
        valHash = {}
        valSet = set([str(i) for i in range(1,10)])
        for i in valList:
            valHash[i] = valHash.get(i, 0) + 1
        isValid = True
        for key in valHash:
            if key in valSet and valHash[key] > 1:
                isValid = False
        return isValid