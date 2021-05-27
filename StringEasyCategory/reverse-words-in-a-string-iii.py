class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        substrs=s.split(" ")
        t=[]
        
        for i in substrs:
            j=i[::-1]
            t.append(j)
        
        # print (t)
        
        t_string=' '.join(t)
        return t_string
