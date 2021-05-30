class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=n/2
        arr=[]
        
        for i in range(1,l+1):
            arr.append(i)
            arr.append(-i)
        
        if(n%2==0):
            return arr
        else:
            arr.append(0)
            return arr
