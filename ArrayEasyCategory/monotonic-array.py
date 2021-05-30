class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if(A==sorted(A) or A==sorted(A,reverse=True)):
            return True
        else:
            return False
