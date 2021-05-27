class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_arr=[]
        sub_arr_2=[]
        
        for i in s:
            if(i.isdigit()):
                sub_arr.append(i)
        
        if(sub_arr):
            max_sub=max(sub_arr)
        
        # sub_arr.remove(max_sub)
        
            for i in sub_arr:
                if(i<max_sub):
                    sub_arr_2.append(i)
        
            if(sub_arr_2):
                return max(sub_arr_2)
            else:
                return -1
        else:
            return -1
