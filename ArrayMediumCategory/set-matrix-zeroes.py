class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rownum=[]
        colnum=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    rownum.append(i)
                    colnum.append(j)
        
        
        for i in range(len(matrix)):
            for k in rownum:
                if(i==k):
                    for j in range(len(matrix[0])):
                        matrix[i][j]=0
        
        for j in range(len(matrix[0])):
            for k in colnum:
                if(j==k):
                    for i in range(len(matrix)):
                        matrix[i][j]=0
        
        return matrix
