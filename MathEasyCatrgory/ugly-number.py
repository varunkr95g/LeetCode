class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=0

        if(n>0):
            while(n>1):
                if(n%2==0):
                    n=n//2
                elif(n%3==0):
                    n=n//3
                elif(n%5==0):
                    n=n//5
                else:
                    count=1
                    break
            if(count):
                return False
            else:
                return True
        else:
            return False
