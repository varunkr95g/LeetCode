class Solution(object):
    def fib(self, N):
        """
        :type n: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
            
