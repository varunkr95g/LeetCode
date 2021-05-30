class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rev_arr=arr[::-1]
        final_arr=[]
        
        # print rev_arr
        
        final_arr.append(-1)
        
        for j in range(1,len(rev_arr)):
            final_arr.append(max(rev_arr[:j]))
        
        return final_arr[::-1]
