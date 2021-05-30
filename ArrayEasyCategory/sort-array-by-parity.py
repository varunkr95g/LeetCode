class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        sub_arr_even=[]
        sub_arr_odd=[]
        sub_arr=[]
        
        for i in range(len(A)):
            if(A[i]%2==0):
                sub_arr_even.append(A[i])
            else:
                sub_arr_odd.append(A[i])
        
        sub_arr=sub_arr_even+sub_arr_odd
        
        return sub_arr
