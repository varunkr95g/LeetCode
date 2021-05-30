class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr=[]
        xor=0
        
        for i in range(n):
            arr.append(start + 2*i)
        
        for j in range(len(arr)):
            xor^=(arr[j])
        
        return (xor)
