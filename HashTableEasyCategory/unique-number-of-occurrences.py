class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sub_arr=[]
        dic={}
        
        for i in arr:
            if (i in dic):
                dic[i]+=1
            else:
                dic[i]=1
        
        # print (dic)
        
        for i in dic.values():
            sub_arr.append(i)
        
        # print (sub_arr)
        
        sub_arr_2=list(set(sub_arr))
        
        if(len(sub_arr_2)==len(sub_arr)):
            return True
        else:
            return False
