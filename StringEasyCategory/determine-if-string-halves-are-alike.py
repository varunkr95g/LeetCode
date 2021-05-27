class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls=s.lower()



        ls1=ls[:len(ls)/2]
        ls2=ls[len(ls)/2:len(ls)]
        count1=0
        count2=0
        
        for i in ls1:
            if (i in ('a','e','i','o','u')):
                count1+=1
        
        # print (count1)
        
        for i in ls2:
            if (i in ('a','e','i','o','u')):
                count2+=1
        
        # print count2
        
        if count1==count2:
            return True
        else:
            return False
