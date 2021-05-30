class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n>0):
            count = 0

            while n>1:
                if(n%2==0):
                    n=n//2
                else:
                    count=1
                    break

            if(count) :
                return False

            else:
                return True
        else:
            return False
