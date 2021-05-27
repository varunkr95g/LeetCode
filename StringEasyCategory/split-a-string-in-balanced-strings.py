class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance=0
        count=0
        
        for i in s:
        
            if(i=='L'):
                count+=1
            else:
                count-=1
        
            if(count==0):
                balance+=1
        
        return balance
