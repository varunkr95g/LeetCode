class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        listnum=list(str(n))
        productn=1
        sumn=0
        
        for i in listnum:
            productn*=int(i)
            sumn+=int(i)
        
        return productn-sumn
