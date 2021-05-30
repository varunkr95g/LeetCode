class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        sub_arr=[]

        for i in range(len(arr)):
            sub_arr.append(arr[i])
            if(arr[i]==0):
                sub_arr.append(0)
        
        # print (sub_arr)
        
        for i in range(len(arr)):
            arr[i]=sub_arr[i]
        
        # print(arr)
