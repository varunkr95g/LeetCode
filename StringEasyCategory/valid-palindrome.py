class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t=""

        for i in s:
            if(i.isalnum()):
                t+=i
        
        t=t.lower()
        
        t_rev=t[::-1]
        
        if(t==t_rev):
            return True
        else:
            return False
