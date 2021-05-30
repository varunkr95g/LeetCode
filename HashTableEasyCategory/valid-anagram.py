class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub_arr=[]
        if(len(s)!=len(t)):
            return False
        else:

            lists = list(s)
            listt = list(t)
        
            lists.sort()
            listt.sort()
        
            for i in range(len(lists)):
                if(lists[i]==listt[i]):
                    sub_arr.append(listt[i])
        
            if (len(sub_arr) == len(listt)):
                return True
            else:
                return False
