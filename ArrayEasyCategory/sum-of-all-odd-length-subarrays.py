class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sub_arr=[]
        total=0
        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                sub_arr.append(arr[i:j])
        
        # print (sub_arr)
        
        # print (sub_arr[1][1])  #11
        
        for i in range(len(sub_arr)):
            if (len(sub_arr[i])%2!=0):
                for j in range(len(sub_arr[i])):
                    total+=sub_arr[i][j]
        
        return total
