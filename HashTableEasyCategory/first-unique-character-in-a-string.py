class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lists=list(s)

        dictionary={}
        sub_arr=''
        
        for i in lists:
            if(i not in dictionary):
                dictionary[i]=1
            else:
                dictionary[i]+=1
        
        # print dictionary
        
        for i in lists:
            if(dictionary[i]==1):
                sub_arr=i
                break
        
        if sub_arr:
            return lists.index(sub_arr)
        else:
            return -1
