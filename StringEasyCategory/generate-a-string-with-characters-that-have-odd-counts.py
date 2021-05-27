class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        sub_arr=[]

        if(n%2==0):
            for i in range(n-1):
                sub_arr.append("a")
        
            sub_arr.append("b")
        else:
            for i in range(n):
                sub_arr.append("a")
        
        
        
        return ''.join(sub_arr)
