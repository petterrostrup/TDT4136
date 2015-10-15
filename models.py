class board():
    self.numRows = None;
    self.numCols = None;
    self.boardMatrix = None;

    def __init__(rows, cols):
        self.numRows = rows;
        self.numCols = cols;
        self.boardMatrix = [[0 for col in range(numCols)] for row in range(numRows)]


    def getCols():
        return [self.matrix[y][x] for y in range(numCols)] for x in range(numRows)]

    def getRows():
        return boardMatrix;

    def getDiagonal()::
        leftDiagonals = []
        rightDiagonals = []

        # For the number of adjacent diagonals in a matrix of size self.M * self.M
        for p in range(0, self.M * 2 - 1):

            left = []
            right = []

            # Dynamic boundries to prevent indexes off the matrix
            for q in range(max(0, p - self.M + 1), min(p, self.M - 1) + 1):

                # Add the right-up diags
                right.append(self.matrix[p - q][q])
                # Add the left-up diags
                left.append(self.matrix[p - q][self.M - 1 - q])

            # Add them to their respective lists
            if left:
                leftDiagonals.append(left)
            if right:
                rightDiagonals.append(right)

        return leftDiagonals, rightDiagonals

class eggBoard(board):
    self.K = None;

    def __init__(rows, cols, K):
        self.numRows = rows;
        self.numCols = cols;
        self.boardMatrix = [[0 for col in range(numCols)] for row in range(numRows)]
        self.K = K;

    def checkRows():
        return [K - sum(row) for row in self.boardMatrix];

    def checkColumns():
        return [K - sum(col) for col in self.get_columns()]

    
