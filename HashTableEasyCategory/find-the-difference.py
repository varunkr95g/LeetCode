class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lists = list(s)
        listt = list(t)
        lists.sort()
        listt.sort()
        lists.append(" ")
        # print (lists)
        # print (listt)
        listm = []
        m = ""
        
        
        
        for i in range(len(lists)):
            if (lists[i] != listt[i]):
                listm.append(listt[i])
        
        m = ''.join(listm)
        
        return m[0]
