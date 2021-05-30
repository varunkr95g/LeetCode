class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n>0):
            count = 0

            while n>1:
                if(n%3==0):
                    n=n//3
                else:
                    count=1
                    break

            if(count) :
                return False

            else:
                return True
        else:
            return False
