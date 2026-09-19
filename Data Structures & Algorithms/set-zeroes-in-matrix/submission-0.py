class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        reg_m = [False for _ in range(len(matrix))]
        reg_n = [False for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    reg_m[i] = True
                    reg_n[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if reg_m[i] == True or reg_n[j] == True:
                    matrix[i][j] = 0
        