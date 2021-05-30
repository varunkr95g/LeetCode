class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)
        sum=0
        
        
        if (n%2!=0):
            k = 0
            for i in range(len(mat)):
                sum+=mat[i][i]
                # print (mat[i][i])
            for j in range(len(mat)-1,-1,-1):
                k=(n-j-1)
                sum+=mat[k][j]
        
            sum-=mat[n/2][n/2]
        
        if (n%2==0):
            k = 0
            for i in range(len(mat)):
                sum += mat[i][i]
                # print (mat[i][i])
            for j in range(len(mat) - 1, -1, -1):
                k = (n - j - 1)
                sum += mat[k][j]
        
        
        
        return sum
