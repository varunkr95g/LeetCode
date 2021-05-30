class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()


        diff_arr=[]
        
        output_arr=[]
        
        
        
        for i in range(1,len(arr)):
            diff_arr.append(arr[i]-arr[i-1])
        
        min_diff=min(diff_arr)
        
        # print diff_arr
        # print min_diff
        
        for i in range(1,len(arr)):
            sub_arr = []
            if(arr[i]-arr[i-1])==min_diff:
                sub_arr.append(arr[i-1])
                sub_arr.append(arr[i])
        
        
            if(len(sub_arr)>0):
                output_arr.append(sub_arr)
        
        # for i in output_arr:
        #     if (len(i)>0):
        #         output_arr_2.append(i)
        
        
        
        return output_arr
