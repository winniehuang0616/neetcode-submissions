class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        index = list()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    index.append([r,c])
        
        for ix in index:
            r, c = ix[0], ix[1]
            matrix[r] = [0] * len(matrix[r])
            for k in range(len(matrix)):
                matrix[k][c] = 0
        
                    
        