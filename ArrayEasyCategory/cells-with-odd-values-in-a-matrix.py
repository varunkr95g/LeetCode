class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        arr=[[0 for j in range(m)] for i in range(n)]

        indices = [[1,1],[0,0]]
        # print (arr)
        
        for i in range(len(indices)):
            # [0,1]
            for j in range(m):
                arr[indices[i][0]][j]+=1
            for j in range(n):
                arr[j][indices[i][1]]+= 1
        
        # print (arr)
        count=0
        
        for i in range(n):
            for j in range(m):
                if((arr[i][j])%2!=0):
                    count+=1
        
        
        return count

        # count=0
        # row=[0]*n
        # col=[0]*m
        # for x,y in indices:
        #     row[x]+=1
        #     col[y]+=1
        # for i in range(n):
        #     for j in range(m):
        #         if (row[i]+col[j])%2==1:
        #             count+=1
        # return count
